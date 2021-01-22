# Trace History

This is a python Command Line Interface (CLI) for performing Rohde & Schwarz (R&S) Vector Network Analyzer (VNA) measurements with trace history.

## Command Line Interface

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

## Requirements

This project was validated with python version `3.8.5` `x64` on `macOS` Catalina version `10.15.7`.

## Scripts

There is a start script and several build scripts in the `scripts` folder.

Most scripts are provided for both Bash (macOS, Linux) and Windows Batch file.
