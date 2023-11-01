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

## Command Line Interface

To see a list of possible settings, access the help menu from the command line as follows:

`trace-history --help`

You should see the following output:

```comment
usage: trace-history [-h] [--quiet] [--version] [--ip-address IP_ADDRESS]
         [--log-file LOG_FILE] [--timeout-ms TIMEOUT_MS] [--set-file SET_FILE]
         [--data-path DATA_PATH]
         sweep_count

positional arguments:
  sweep_count

optional arguments:
  -h, --help               show this help message and exit
  --quiet                  do not print to stdout
  --version                show program's version number and exit
  --ip-address IP_ADDRESS  default: localhost
  --log-file LOG_FILE      default: vna.log
  --timeout-ms TIMEOUT_MS  default: 120000
  --set-file SET_FILE
  --data-path DATA_PATH    default: current working directory
```

## Example

See [example/README.md](./example/README.md) for an example use of `trace-history`.
