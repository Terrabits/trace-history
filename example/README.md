# Trace History Example

This example uses the Rohde & Schwarz `trace-history` command line utility to save several hundred sweeps of Trace History data for each Vector Network Analyzer (VNA) set file (or measurement setup) in a list.

## Requirements

-   Python        ~= 3.4
-   trace_history ~= 1.4
-   Rohde & Schwarz VNA

## Install trace-history

This example requires installing the `trace-history` command line utility per the README.

If it is installed correctly, you should be able to execute the following command from the command line to print the `--help` menu:

`trace-history --help`

You should see the following:

```comment
usage: trace-history [-h] [--quiet] [--version] [--ip-address IP_ADDRESS]
                     [--log-file LOG_FILE] [--timeout-ms TIMEOUT_MS]
                     [--set-file SET_FILE] [--data-path DATA_PATH]
                     sweep_count

positional arguments:
  sweep_count

options:
  -h, --help            show this help message and exit
  --quiet               do not print to stdout
  --version             show program's version number and exit
  --ip-address IP_ADDRESS
                        default: localhost
  --log-file LOG_FILE   default: vna.log
  --timeout-ms TIMEOUT_MS
                        default: 120000
  --set-file SET_FILE
  --data-path DATA_PATH
                        default: current working directory
```

## Edit Constants

To make the script work for your particular setup, edit the constants starting on line 6 of [__main__.py](./__main__.py):

```python
# constants
IP_ADDRESS  = 'localhost'
SWEEP_COUNT = 100
SET_FILES   = ["setup1", "setup2", "setup3"]
```

`IP_ADDRESS` should contain the host name or IP address of the VNA.

`SWEEP_COUNT` can be modified to change the number of sweeps of trace history that are captured.

`SET_FILES` should be edited to reference set files saved to the VNA.

Note that set files include any calibrations that were applied.

## Run

To run the script, execute the following from the command line:

```shell
cd path/to/trace-history/example
python .
```

If the script is successful, timing results and trace history data should be saved to the `data/` folder.
