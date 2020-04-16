@echo off
setlocal
set PYTHONPATH=%cd%
python core/simulate.py %1
endlocal