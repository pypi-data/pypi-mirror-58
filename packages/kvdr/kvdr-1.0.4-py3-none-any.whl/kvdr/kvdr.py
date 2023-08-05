#!/usr/bin/env python3
"""KVDR - Key/Value Dump and Restore

Usage:
  kvdr dump [--file=<file_name> | --screen] [-v | --verbose] <redis_url>
  kvdr load (--file=<file_name>) [--dry-run] [-v | --verbose] <redis_url>
  kvdr --dry-run
  kvdr (-h | --help)
  kvdr --version

Options:
  -h --help           Show this screen.
  --version           Show version.
  --screen            Dump to the console instead of file.
  --file=<file_name>  A file where we store dumped Redis records. Default: "redis.dump"
  --dry-run           A trial run. Works only for the loading operation.
  -v --verbose        Add some extra information to the output.

Examples:
  kvdr dump --file=redis13.backup redis://admin:BABADEDAuikxWx0oPZYfPE3IXJ9BVlSC@localhost:6379/13
  kvdr load --file=redis13.backup redis://:BABADEDAuikxWx0oPZYfPE3IXJ9BVlSC@localhost:6379/3

"""
import json
from docopt import docopt
from .util import version, get_redis_client


def main():
    cmdargs = docopt(__doc__, version=version())

    # Let's get the verbosity flag first
    a_verbose: bool = cmdargs["--verbose"]
    verbose_output: bool = a_verbose
    verbosity_level: int = 0
    if verbose_output:
        verbosity_level = 1
        print("----")
        print(cmdargs)

    a_redis_url: str = cmdargs["<redis_url>"]
    a_console_out: bool = cmdargs["--screen"]
    a_dry_run: bool = cmdargs["--dry-run"]
    a_file_name: str = "redis.dump" if not cmdargs["--file"] else cmdargs["--file"]

    if cmdargs["dump"]:
        from .dump import dump

        a_base64_encoded = False if a_console_out else True
        result = dump(get_redis_client(a_redis_url),
                      file_name=a_file_name, console_out=a_console_out,
                      base64_encoded=a_base64_encoded, verbosity=verbosity_level)
        print("")  # dump() does not output EOL, so we have to do it here
        print(f"{result['count']} keys dumped to the '{a_file_name}' in {result['elapsed']} sec.")

    if cmdargs["load"]:
        from .load import load
        result = {}
        redis_client = get_redis_client(a_redis_url)
        if redis_client:
            redis_client.set("hello", "world")
        with open(a_file_name, "r") as rfile:
            result = load(rfile, redis_client, a_dry_run, verbosity=verbosity_level)

        print(f"{result['loaded']} keys loaded from the '{a_file_name}' file in {result['elapsed']} sec.")
        if a_dry_run:
            print(json.dumps(result["data"], indent=2))
        else:
            print(result)


if __name__ == '__main__':
    main()
