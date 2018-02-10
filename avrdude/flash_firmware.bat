@echo off
if "%1"=="" goto :usage 
if "%2"=="" (
  echo Error! No hex file provided.
  goto :usage
)
if not exist "%2" (
  echo %2 does not exist
  goto :eof
)
if not exist avrdude.exe (
  echo Error! This script must be executed within the "avr" directory
  goto :eof
)
avrdude.exe -c stk500v2 -b 115200 -p atmega2560 -P \\.\%1 -U flash:w:%2 -C avrdude.conf
goto :eof

:usage
echo Usage: flash_firmware.bat COM_PORT HEX_FILE

:eof
