@echo off
setlocal
set PYTHONPATH=%cd%
python core/simulate.py %*
endlocal