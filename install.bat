@echo off

echo Installing pyXPArduino
echo This install script requires you to have python 3 and pip 3 installed
  
CHOICE /M "This will replace all of your existing configuration files, are you sure you want to continue?"

If ERRORLEVEL 2 GOTO NO
If ERRORLEVEL 1 GOTO INSTALL


GOTO END

:INSTALL
mkdir "./config"
copy initial_config\*.* config
pip3 install pyxpudpserver
pip3 install PyQt5
pip3 install pyserial

:NO
echo no changes made
:END
echo Done, bye!

 
 