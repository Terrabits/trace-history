# Trace History

Trace History is a command line utility for using the Rohde & Schwarz (R&S) Vector Network Analyzer (VNA) Trace History feature.

As of `1 Nov 2023`, the Trace History feature is only available via SCPI commands. This utility provides a simple interface that can be used on any platform on the command line.

## Requirements

-   Python       ~= 3.4
-   rohdeschwarz ~=1.9.2.dev1
-   si-prefix    ~=1.2

## Install

To install the `trace-history` command line utility, first clone the project repo then run pip install as follows:

```shell
cd path/to/trace-history
pip install .
```

## CLI

The command line interface (CLI) help menu can be printed with the `--help` flag:

`trace-history --help`

You should see the following output:

```comment
usage: trace-history [-h] [--quiet] [--version] [--ip-address IP_ADDRESS]
                     [--timeout-ms TIMEOUT_MS] [--set-file SET_FILE]
                     [--data-path DATA_PATH]
                     sweep_count

positional arguments:
  sweep_count

options:
  -h, --help            show this help message and exit
  --quiet               do not print to stdout
  --version             show program's version number and exit
  --ip-address IP_ADDRESS
                        default: localhost
  --timeout-ms TIMEOUT_MS
                        default: 120000
  --set-file SET_FILE
  --data-path DATA_PATH
                        default: current working directory
```

## Example

See [example/README.md](./example/README.md) for an example use of `trace-history`.
