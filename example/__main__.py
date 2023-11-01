from   io       import StringIO
from   subprocess import PIPE, run, STDOUT
import sys


# constants
IP_ADDRESS  = 'localhost'
SWEEP_COUNT = 100
SET_FILES   = ["setup1", "setup2", "setup3"]


# command format string
COMMAND = 'trace-history --ip-address {IP_ADDRESS} --set-file {set_file} --data-path data {SWEEP_COUNT}'


def main():

    for set_file in SET_FILES:

        # call trace-history
        command = COMMAND.format_map({
            'IP_ADDRESS':  IP_ADDRESS,
            'set_file':    set_file,
            'SWEEP_COUNT': SWEEP_COUNT
        })
        result = run(command, shell=True)


if __name__ == '__main__':
    main()
