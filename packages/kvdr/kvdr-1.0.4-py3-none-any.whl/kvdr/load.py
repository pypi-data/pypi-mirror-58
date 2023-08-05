# standard library
from base64 import b64decode
from datetime import datetime

# 3rd party
from redis import Redis

# Description of the keys used:
# DK: decoded key
# PV: value of the primary key (i could not bother finding a better name)
# EX: expiration time (in seconds, -1 means never expires)
# MT: "my time" - the current time
# RR: record start
# TT: type of data
# KK: "primary" key


def out_rec_to_dict(record: dict, destination: dict):
    result = {"expired": 0, "written": 0}

    if (destination is not None) and (record is not None):
        if ("DK" in record) and ("PV" in record):
            destination[record["DK"]] = record["PV"]
            result["written"] += 1

    return result


def write_to_redis(record: dict, redis_client: Redis = None):
    rtype = record["TT"]
    pkey = record["DK"]
    if rtype == "string":
        redis_client.set(pkey, record["PV"])
    elif rtype == "list":
        values = record["PV"]
        # TODO: do this in bulk of, say, 1000 (configurable?) elements instead of doing it like this
        redis_client.lpush(pkey, *values)
    elif rtype == "set":
        values = record["PV"]
        # TODO: do this in bulk of, say, 1000 (configurable?) elements instead of doing it like this
        redis_client.sadd(pkey, *values)
    elif rtype == "hash":
        # for k, v in record["PV"].items():
        #     redis_client.hset(pkey, k, v)
        # TODO: do this in bulk of, say, 1000 (configurable?) elements instead of doing it like this
        kvals = record["PV"]
        redis_client.hmset(pkey, kvals)
    elif rtype == "zset":
        # TODO: do this in bulk of, say, 1000 (configurable?) elements instead of doing it like this
        kvals = record["PV"]
        print(kvals)
        redis_client.zadd(pkey, kvals)
    else:
        print(f"Unsupported type {rtype}")

    # Update the expire time
    if record["EX"] != -1:
        redis_client.expire(pkey, record["EX"])


def write_rec(record: dict, redis_client: Redis = None):
    result = {"expired": 0, "written": 0}

    if record:
        expired = True
        if record["EX"] == -1:
            expired = False
        else:
            cur_ts = datetime.utcnow().timestamp()
            ex_ts = record["MT"] + record["EX"]
            diff = ex_ts - cur_ts
            if diff > 0:
                expired = False
            else:
                expired = True
        if expired:
            print("expired: ", record["DK"])
            result["expired"] += 1
        else:
            write_to_redis(record, redis_client)
            result["written"] += 1

    return result


def load(rfile, redis_client: Redis, build_dict: bool = False, verbosity: int = 0) -> dict:
    start_dt = datetime.now()
    cnt_loaded = 0
    cnt_expired = 0
    rec = None
    out_dict = {} if build_dict else None

    list_value = []

    hash_el_key = ""
    hash_value = {}

    set_value = set()

    zset_el_key = ""
    zset_value = {}

    for line in rfile:
        line = line.strip()
        # is the line that indices record start
        if line.startswith("RR:"):
            # If the record has been created previously, write it
            if build_dict:
                wres = out_rec_to_dict(rec, out_dict)
            else:
                wres = write_rec(rec, redis_client)

            # Update stats
            cnt_loaded += wres["written"]
            cnt_expired += wres["expired"]

            # Reset the record, so that we may build it while we parse
            rec = {"DK": "", "PV": ""}

        if line.startswith("KK:"):
            # decoded key
            rec["DK"] = b64decode(line[3:]).decode("utf-8")
            # key as it is in the dump file (base64 encoded)
            rec["KK"] = line[3:]

            # If user wants verbose output, print the decoded key
            if verbosity > 0:
                print(rec["DK"])

        if line.startswith("MT:"):
            rec["MT"] = float(line[3:])

        if line.startswith("EX:"):
            rec["EX"] = int(line[3:])

        if line.startswith("TT:"):
            hash_el_key, hash_value, list_value, set_value, zset_el_key, zset_value = _handle_type_record(
                hash_el_key, hash_value, line, list_value, rec, set_value, zset_el_key, zset_value)

        if line.startswith("VV:"):
            # string value
            string_value = b64decode(line[3:]).decode("utf-8")
            rec["PV"] = string_value

        if line.startswith("LV:"):
            # list value
            list_value.append(b64decode(line[3:]).decode("utf-8"))
            rec["PV"] = list_value  # probably redundant...

        if line.startswith("HK:"):
            # hash key
            hash_el_key = b64decode(line[3:]).decode("utf-8")

        if line.startswith("HV:"):
            # hash value
            hash_el_value = b64decode(line[3:]).decode("utf-8")
            # by now we have both key and value, so we can set it
            hash_value[hash_el_key] = hash_el_value
            rec["PV"] = hash_value  # probably redundant...

        if line.startswith("SV:"):
            # set key
            set_value.add(b64decode(line[3:]).decode("utf-8"))
            rec["PV"] = list(set_value)  # probably redundant...

        if line.startswith("ZK:"):
            # key of the sorted-set element
            zset_el_key = b64decode(line[3:]).decode("utf-8")

        if line.startswith("ZV:"):
            # value (score) of the sorted-set element
            zset_el_value = float(b64decode(line[3:]).decode("utf-8"))
            # by now we have both key and value, so we can set it
            zset_value[zset_el_key] = zset_el_value
            rec["PV"] = zset_value  # probably redundant...

    end_dt = datetime.now()
    secs = (end_dt - start_dt).total_seconds()

    result = {"loaded": cnt_loaded,
              "expired": cnt_expired,
              "elapsed": secs}

    # Only if build_dict is True we set this value in the result
    if build_dict:
        result["data"] = out_dict

    return result


def _handle_type_record(hash_el_key, hash_value, line, list_value, rec, set_value, zset_el_key, zset_value):
    rtype = line[3:]
    rec["TT"] = rtype
    if rtype.startswith("string"):
        string_value = ""
        rec["PV"] = string_value
    if rtype.startswith("hash"):
        hash_el_key = ""
        hash_value = {}
        rec["PV"] = hash_value
    if rtype.startswith("list"):
        list_value = []
        rec["PV"] = list_value
    if rtype.startswith("set"):
        set_value = set()
        rec["PV"] = list(set_value)
    if rtype.startswith("zset"):
        zset_el_key = ""
        zset_value = {}
        rec["PV"] = zset_value
    return hash_el_key, hash_value, list_value, set_value, zset_el_key, zset_value
