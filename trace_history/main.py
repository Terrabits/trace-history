#!/usr/bin/env python
from   .command_line                import parse_args
import csv
from   pathlib                      import Path
from   rohdeschwarz.instruments.vna import Vna
from   si_prefix                    import si_format
import sys


def main():
    # parse cli
    args = parse_args()


    # connect to vna
    vna = Vna()
    try:
        vna.open_tcp(args.ip_address)
    except (TimeoutError, ConnectionError):
        message = f'error: could not connect to vna at "{args.ip_address}"'
        print(message, file=sys.stderr)
        sys.exit(1)


    # measure, save, keep timing info
    total_sweep_time_s = measure_and_save_trace_history(
        vna,
        args.sweep_count,
        args.set_file,
        args.timeout_ms,
        args.data_path
    )


    # verbose?
    if not args.quiet:
        time_per_sweep_s = total_sweep_time_s / args.sweep_count
        print(f'total time: {si_format(total_sweep_time_s, precision=3)}s')
        print(f'per sweep:  {si_format(time_per_sweep_s,   precision=3)}s')


    # success
    sys.exit(0)


if __name__ == '__main__':
    main()
