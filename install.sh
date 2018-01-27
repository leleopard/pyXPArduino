#!/bin/bash

echo "Installing pyXPArduino"
echo "This install script requires you to have python 3 and pip 3 installed"
echo "This will replace all of your existing configuration files, are you sure you want to continue? [y/n]"
read RESPONSE

if [ "$RESPONSE" = "y" ]; then
  mkdir "./config"
  cp -a ./initial_config/. ./config/
  pip3 install pyxpudpserver
  pip3 install PyQt5
  pip3 install pyserial
  echo "Done!"
fi
