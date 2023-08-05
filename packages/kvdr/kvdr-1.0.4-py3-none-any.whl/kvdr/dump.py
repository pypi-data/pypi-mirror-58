# standard library
from base64 import b64encode
from datetime import datetime

# 3rd party
from redis import Redis

# our stuff
from .util import out


def _out_record_header(cnt, console_out=False, verbosity=0, rfile=None):
    # record starts
    out("RR:------------------- ", str(cnt), out_file=rfile)
    if verbosity > 0 and not console_out:
        print("RR:------------------- ", cnt)


def _out_key_name(key, console_out=False, verbosity=0, rfile=None, base64_encoded: bool = True):
    if base64_encoded:
        b64key = b64encode(key).decode("utf-8")
        out("KK:", b64key, out_file=rfile)
    else:
        out("KK:", key, out_file=rfile)
    if verbosity > 0 and not console_out:
        out("KK:", key.decode("utf-8"))


def _out_ttl(key, redis_client, rfile=None):
    ttl = redis_client.ttl(key)
    mytime = datetime.utcnow().timestamp()
    # We output our time, so that when we eventually decide to load the data from this dump we can skip
    # expired records.
    out("MT:", str(mytime), out_file=rfile)
    out("EX:", str(ttl), out_file=rfile)


def _out_record_type(key_type, rfile=None):
    out("TT:", key_type, out_file=rfile)


def _out_string(key, redis_client, base64_encoded: bool = True, rfile=None):
    value = redis_client.get(key)
    if base64_encoded:
        value = b64encode(value)
    out("VV:", value.decode("utf-8"), out_file=rfile)


def _out_hash(key, redis_client, base64_encoded: bool = True, rfile=None):
    for hkey, hval in redis_client.hscan_iter(key):
        kk = hkey
        vv = hval

        if base64_encoded:
            kk = b64encode(hkey)
            vv = b64encode(hval)

        out("HK:", kk.decode("utf-8"), out_file=rfile)
        out("HV:", vv.decode("utf-8"), out_file=rfile)


def _out_set(key, redis_client, base64_encoded: bool = True, rfile=None):
    for sval in redis_client.sscan_iter(key):
        vv = sval

        if base64_encoded:
            vv = b64encode(sval)

        out("SV:", vv.decode("utf-8"), out_file=rfile)


def _out_sorted_set(key, redis_client, base64_encoded: bool = True, rfile=None):
    for zkey, zval in redis_client.zscan_iter(key):
        kk = zkey
        vv = str(zval)

        if base64_encoded:
            kk = b64encode(zkey)
            vv = b64encode(str(zval).encode("utf-8")).decode("utf-8")  # zval is a 64bit float

        out("ZK:", kk.decode("utf-8"), out_file=rfile)
        out("ZV:", vv, out_file=rfile)


def _out_list(key, redis_client, base64_encoded: bool = True, rfile=None):
    for el in redis_client.lrange(key, 0, -1):
        value = el
        if base64_encoded:
            value = b64encode(value)
        out("LV:", value.decode("utf-8"), out_file=rfile)


def _out_unknown(key, redis_client, base64_encoded: bool = True, rfile=None):
    kk = key
    vv = redis_client.get(key)
    if base64_encoded:
        kk = b64encode(key)
        vv = b64encode(vv)
    out("UK:", kk.decode("utf-8"), out_file=rfile)
    out("UV:", vv.decode("utf-8"), out_file=rfile)


def _out_typechar(rtype: str):
    """
    The idea is to use this function to print a character whenever key/value has been dumped, so the user
    sees some progress...
    """
    if rtype == "string":
        typechar = "T"
    elif rtype == "hash":
        typechar = "H"
    elif rtype == "set":
        typechar = "S"
    elif rtype == "zset":
        typechar = "Z"
    elif rtype == "list":
        typechar = "L"
    else:
        typechar = "U"
    print(typechar, end="")


def dump(redis_client: Redis, file_name: str = None, console_out: bool = False, limit: int = 2**31,
         verbosity: int = 0, base64_encoded: bool = True) -> dict:
    start_dt = datetime.now()
    kvdr_fileobj = None
    dumped_to_file = False
    if file_name and not console_out:
        dumped_to_file = True
        kvdr_fileobj = open(file_name, "w")

    cnt = 0
    # scan all the Redis keys
    for key in redis_client.scan_iter():
        cnt += 1
        _out_record_header(cnt, console_out, verbosity, rfile=kvdr_fileobj)

        _out_key_name(key, console_out, verbosity, rfile=kvdr_fileobj)

        _out_ttl(key, redis_client, rfile=kvdr_fileobj)

        key_type = redis_client.type(key).decode("utf-8")
        # _out_typechar(key_type)
        _out_record_type(key_type, rfile=kvdr_fileobj)

        if key_type == "string":
            _out_string(key, redis_client, base64_encoded, rfile=kvdr_fileobj)
        elif key_type == "hash":
            _out_hash(key, redis_client, base64_encoded, rfile=kvdr_fileobj)
        elif key_type == "set":
            _out_set(key, redis_client, base64_encoded, rfile=kvdr_fileobj)
        elif key_type == "zset":
            _out_sorted_set(key, redis_client, base64_encoded, rfile=kvdr_fileobj)
        elif key_type == "list":
            _out_list(key, redis_client, base64_encoded, rfile=kvdr_fileobj)
        else:
            print(f"Unsupported type '{key_type}'")
            _out_unknown(key, redis_client, base64_encoded, rfile=kvdr_fileobj)

        if cnt > limit:
            break

    if dumped_to_file:
        kvdr_fileobj.close()

    end_dt = datetime.now()
    secs = (end_dt - start_dt).total_seconds()

    # Passed through all the keys, return dictionary with some information about the dump process.
    return {"count": cnt, "elapsed": secs}
