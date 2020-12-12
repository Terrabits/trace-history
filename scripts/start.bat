@echo off
SET ROOT_DIR=%~dp0..


setlocal
cd %ROOT_DIR%


rem start
python . %*
