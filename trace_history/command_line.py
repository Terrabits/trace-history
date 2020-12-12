import argparse
import os
from   pathlib import Path


# timeout constants
ONE_SECOND_MS = 1000
ONE_MIN_MS    = 60 * ONE_SECOND_MS
TWO_MINS_MS   =  2 * ONE_MIN_MS


def parse_args():
    current_path = os.getcwd()

    # define command line interface (cli)
    parser = argparse.ArgumentParser()
    parser.add_argument('--quiet', action='store_true')
    parser.add_argument('--ip-address',           default='localhost')
    parser.add_argument('--log',                  default='vna.log')
    parser.add_argument('--timeout-ms', type=int, default=TWO_MINS_MS)
    parser.add_argument('--set-file')
    parser.add_argument('--data-path',            default='.')
    parser.add_argument('sweep_count',  type=int)

    # parse cli
    args = parser.parse_args()

    # validate and resolve data path
    args.data_path = Path(args.data_path).resolve()
    if not args.data_path.exists():
        raise Exception(f'{str(args.data_path)} does not exist')

    return args
