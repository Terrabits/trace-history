@echo off
SET ROOT_DIR=%~dp0


setlocal
cd %ROOT_DIR%


rem parameters
SET SWEEP_COUNT=100
SET RUN_COUNT=100

rem mkdir
SET    DATA_PATH=sweep_count_%SWEEP_COUNT%
mkdir %DATA_PATH%

rem call trace-history
for /L %%i in (1, 1, 100) do (
  trace-history\trace-history.exe --data-path %DATA_PATH% %SWEEP_COUNT%
)


rem press enter to continue...
echo.
pause
