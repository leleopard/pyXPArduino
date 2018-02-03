pyuic5 mainwindow.ui -o mainwindow.py
pyuic5 pickarduinodialog.ui -o pickarduinodialog.py
pyuic5 confirmationdialog.ui -o confirmationdialog.py
pyuic5 pickXPCommandDialog.ui -o pickXPCommandDialog.py
pyuic5 pickXPDatarefDialog.ui -o pickXPDatarefDialog.py
pyuic5 switchEditForm.ui -o switchEditForm.py
pyuic5 pwmEditForm.ui -o pwmEditForm.py
pyuic5 digOutputEditForm.ui -o digOutputEditForm.py
pyuic5 servoEditForm.ui -o servoEditForm.py
pyuic5 potentiometerEditForm.ui -o potentiometerEditForm.py
pyuic5 rotencoderEditForm.ui -o rotencoderEditForm.py
pyuic5 xpudpconfigdialog.ui -o xpudpconfigdialog.py

pyrcc5 resources.qrc -o ../resources_rc.py