# Trace History

This is a python Command Line Interface (CLI) for performing Rohde & Schwarz (R&S) Vector Network Analyzer (VNA) measurements with trace history.

## Command Line Interface

```comment
usage: trace-history [-h] [--quiet] [--ip-address IP_ADDRESS] [--log LOG]
                     [--timeout-ms TIMEOUT_MS] [--set-file SET_FILE]
                     [--data-path DATA_PATH]
                     sweep_count

positional arguments:
  sweep_count

optional arguments:
  -h, --help            show this help message and exit
  --quiet
  --ip-address IP_ADDRESS
  --log LOG
  --timeout-ms TIMEOUT_MS
  --set-file SET_FILE
  --data-path DATA_PATH
```

## Requirements

This project was validated with python version `3.8.5` `x64` on `macOS` Catalina version `10.15.7`.

## Scripts

There is a start script and several build scripts in the `scripts` folder.

If working on Windows, these scripts can either be used as examples or run with `Git Bash` or `MSYS2`.

## Procedure for Set Files

For instructions on how to generate set files and calibrate, see [doc/procedure-for-set-files/procedure-for-set-files.md](doc/procedure-for-set-files/procedure-for-set-files.md)
