from   .version import VERSION
import argparse
import os
import sys


# timeout constants
ONE_SECOND_MS = 1000
ONE_MIN_MS    = 60 * ONE_SECOND_MS
TWO_MINS_MS   =  2 * ONE_MIN_MS


# for displaying default arguments
default_str = 'default: %(default)s'
default_int = 'default: %(default)d'


def parse_args():
    # define command line interface (cli)
    parser = argparse.ArgumentParser()
    parser.add_argument('--quiet',   action='store_true', help='do not print to stdout')
    parser.add_argument('--version', action='version', version=VERSION)
    parser.add_argument('--ip-address',           default='localhost', help=default_str)
    parser.add_argument('--timeout-ms', type=int, default=TWO_MINS_MS, help=default_int)
    parser.add_argument('--set-file')
    parser.add_argument('--data-path', default='.', help='default: current working directory')
    parser.add_argument('sweep_count',  type=int)

    # parse
    args = parser.parse_args()
    return args
