# pyXPArduino — Claude Code Guide

## Project Overview

pyXPArduino is a Python/PyQt5 desktop application that bridges Arduino microcontrollers with X-Plane flight simulator. It lets users map physical cockpit hardware (switches, potentiometers, servos, rotary encoders) to X-Plane datarefs and commands over USB serial + UDP.

**Version:** 1.3
**License:** GNU GPL v3

## Architecture

```
pyXPArduino/
├── pyXPArduino.py          # Main entry point — app init, main window setup
├── lib/                    # Core business logic
│   ├── Arduino.py          # Arduino thread + communication manager
│   ├── arduinoXMLconfig.py # XML config parser (component definitions)
│   ├── arduinoSerial.py    # Serial port read/write
│   ├── ardUpload.py        # Firmware upload via avrdude
│   └── XPrefData.py        # X-Plane dataref/command reference loader
├── gui/                    # All PyQt5 UI components
│   ├── mainwindow.py/.ui   # Main window
│   ├── pyXP*EditForm.py    # Per-component edit dialogs
│   └── pyXP*Dialog.py      # Other dialogs
├── config/                 # Runtime config (gitignored, copied from initial_config/)
├── initial_config/         # Config templates (committed defaults)
├── instruments/            # Custom instrument XML definitions
├── XPRefFiles/             # X-Plane DataRefs.txt and Commands.txt
└── Resources/              # Arduino firmware hex, UI assets
```

**Key design patterns:**
- Configuration stored as XML files in `config/`
- Arduino communication runs in a dedicated thread (`Arduino.py`)
- X-Plane integration via UDP (`pyxpudpserver` library)
- Qt `.ui` files for layout, `.py` files for logic

## Running the App

```bash
python3 pyXPArduino.py
# or
bash run.sh
```

First-time setup: run `install.bat` (Windows) or manually copy `initial_config/*` → `config/` and install dependencies.

## Dependencies

```bash
pip install PyQt5 pyserial pyxpudpserver numpy Pillow PyOpenGL PyOpenGL_accelerate
```

Hardware: Arduino Mega 2560 connected via USB serial.
Simulator: X-Plane (11+) running on the same or networked machine.

## Building a Distributable

```bash
pyinstaller pyXPArduino.spec --clean
# Output: dist/pyXPArduino/
```

## Configuration

- `config/config.xml` — main app settings (Arduino boards, component mappings)
- `config/UDPSettings.xml` — X-Plane UDP host/port
- `config/configGraphics.ini` — instrument display settings
- `config/logging_conf.json` — per-module log levels

Changes made through the GUI are serialised back to these XML files automatically.

## Logging

Logs go to both console and `pyXPArduino.log`. Configured in `config/logging_conf.json`.

## Testing

```bash
python3 testGraphics.py   # Test instrument rendering / OpenGL
```

No automated test suite — manual testing against a running X-Plane instance is the norm.
