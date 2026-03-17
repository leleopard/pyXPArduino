# pyXPArduino — Agile User Stories

**Baseline version:** 1.0
**Project version:** 1.3
**Date:** 2026-03-17

---

## EPIC 1 — Configuration File Management

**As a user, I want to manage my Arduino configuration files so that I can save, load, and share my hardware setups.**

| ID | Story | Status |
|----|-------|--------|
| CFG-01 | As a user, I can create a new empty Arduino configuration XML file so that I can start a fresh hardware setup. | ✅ Done |
| CFG-02 | As a user, I can open an existing Arduino configuration XML file so that I can resume or modify a previous setup. | ✅ Done |
| CFG-03 | As a user, I can save my current configuration to the XML file so that changes are persisted. | ✅ Done |
| CFG-04 | As a user, I am prompted to save unsaved changes when opening a new file or closing the application so that I do not lose my work accidentally. | ✅ Done |
| CFG-05 | As a user, I can see the current configuration file path in the status bar so that I always know which file I am editing. | ✅ Done |

---

## EPIC 2 — Arduino Board Management

**As a user, I want to add and manage multiple Arduino boards so that I can use them as input/output devices for my cockpit.**

| ID | Story | Status |
|----|-------|--------|
| ARD-01 | As a user, I can auto-discover Arduino boards connected via USB so that I do not need to manually enter serial port details. | ✅ Done |
| ARD-02 | As a user, I can add one or more discovered Arduino boards to my configuration so that they appear in the Arduino tree. | ✅ Done |
| ARD-03 | As a user, I can see the connection status and firmware version of each Arduino board in the tree so that I know which boards are active. | ✅ Done |
| ARD-04 | As a user, I can edit the name, description, and baud rate of an Arduino board so that it is identifiable in my setup. | ✅ Done |
| ARD-05 | As a user, I can remove an Arduino board and all its components from the configuration so that I can clean up unused hardware. | ✅ Done |
| ARD-06 | As a user, I can see the Arduino tree organised into Inputs and Outputs categories so that I can easily navigate my hardware components. | ✅ Done |

---

## EPIC 3 — Switch Configuration (Digital Input)

**As a user, I want to configure physical switches on my Arduino so that they trigger X-Plane commands or set datarefs when pressed or released.**

| ID | Story | Status |
|----|-------|--------|
| SW-01 | As a user, I can add a switch component to an Arduino's input list and assign it to a digital pin so that the hardware input is recognised. | ✅ Done |
| SW-02 | As a user, I can assign one or more X-Plane commands to the switch ON state so that the commands fire when the switch is pressed. | ✅ Done |
| SW-03 | As a user, I can assign one or more X-Plane commands to the switch OFF state so that the commands fire when the switch is released. | ✅ Done |
| SW-04 | As a user, I can mark a command as continuous so that it keeps firing while the switch is held in that state. | ✅ Done |
| SW-05 | As a user, I can assign one or more X-Plane datarefs and values to the switch ON state so that the simulator values are set when the switch is pressed. | ✅ Done |
| SW-06 | As a user, I can assign one or more X-Plane datarefs and values to the switch OFF state so that the simulator values are set when the switch is released. | ✅ Done |
| SW-07 | As a user, I can see the real-time state of a switch in the edit form so that I can verify hardware input is working. | ✅ Done |
| SW-08 | As a user, I can test switch ON and OFF actions directly from the edit form so that I can verify X-Plane integration without operating the physical switch. | ✅ Done |
| SW-09 | As a user, I can remove a switch component from the configuration. | ✅ Done |

---

## EPIC 4 — Potentiometer Configuration (Analog Input)

**As a user, I want to configure potentiometers on my Arduino so that turning a knob updates X-Plane datarefs or triggers commands based on the knob position.**

| ID | Story | Status |
|----|-------|--------|
| POT-01 | As a user, I can add a potentiometer component and assign it to an analog input pin so that the analog value is read. | ✅ Done |
| POT-02 | As a user, I can see the real-time raw value (0–1023) of the potentiometer in the edit form so that I can verify hardware input. | ✅ Done |
| POT-03 | As a user, I can assign a dataref to the potentiometer with a mapping point list so that the raw ADC value is linearly interpolated to the dataref's expected range. | ✅ Done |
| POT-04 | As a user, I can assign X-Plane commands to fire when the potentiometer value falls within specified intervals so that range-based actions are triggered. | ✅ Done |
| POT-05 | As a user, I can test potentiometer actions from the edit form. | ✅ Done |
| POT-06 | As a user, I can remove a potentiometer component from the configuration. | ✅ Done |

---

## EPIC 5 — Rotary Encoder Configuration (Digital Input)

**As a user, I want to configure rotary encoders so that turning a dial sends incremental commands or updates datarefs in X-Plane.**

| ID | Story | Status |
|----|-------|--------|
| ENC-01 | As a user, I can add a rotary encoder component and assign it to two digital pins (A and B) so that rotation direction is detected. | ✅ Done |
| ENC-02 | As a user, I can set the steps-per-notch value (1, 2, or 4) so that the encoder sensitivity matches the hardware. | ✅ Done |
| ENC-03 | As a user, I can enable acceleration so that turning the encoder faster results in faster increments. | ✅ Done |
| ENC-04 | As a user, I can set an acceleration multiplier so that the acceleration behaviour is tuned to my preference. | ✅ Done |
| ENC-05 | As a user, I can assign X-Plane commands to the UP (clockwise) direction so that turning right triggers those commands. | ✅ Done |
| ENC-06 | As a user, I can assign X-Plane commands to the DOWN (anti-clockwise) direction so that turning left triggers those commands. | ✅ Done |
| ENC-07 | As a user, I can test encoder UP and DOWN actions from the edit form. | ✅ Done |
| ENC-08 | As a user, I can remove a rotary encoder from the configuration. | ✅ Done |

---

## EPIC 6 — PWM Output Configuration

**As a user, I want to configure PWM outputs so that Arduino pins output a PWM signal driven by an X-Plane dataref value.**

| ID | Story | Status |
|----|-------|--------|
| PWM-01 | As a user, I can add a PWM output component and assign it to a PWM-capable pin so that the pin outputs a variable signal. | ✅ Done |
| PWM-02 | As a user, I can bind a PWM output to an X-Plane dataref so that the pin's duty cycle reflects the simulator value. | ✅ Done |
| PWM-03 | As a user, I can specify a dataref array index so that a specific element of an array dataref is used. | ✅ Done |
| PWM-04 | As a user, I can see the current dataref value in real-time in the edit form so that I can verify the output mapping. | ✅ Done |
| PWM-05 | As a user, I can remove a PWM output component from the configuration. | ✅ Done |

---

## EPIC 7 — Servo Output Configuration

**As a user, I want to configure servo outputs so that a servo motor position is driven by an X-Plane dataref.**

| ID | Story | Status |
|----|-------|--------|
| SRV-01 | As a user, I can add a servo output component and assign it to a servo-capable pin so that a servo motor is controlled. | ✅ Done |
| SRV-02 | As a user, I can bind a servo to an X-Plane dataref with an optional array index so that the servo position reflects the simulator value. | ✅ Done |
| SRV-03 | As a user, I can see the real-time dataref value in the edit form. | ✅ Done |
| SRV-04 | As a user, I can remove a servo output component from the configuration. | ✅ Done |

---

## EPIC 8 — Digital Output Configuration

**As a user, I want to configure digital outputs so that Arduino pins are driven high or low based on X-Plane dataref values.**

| ID | Story | Status |
|----|-------|--------|
| DIG-01 | As a user, I can add a digital output component and assign it to a digital pin so that the pin state is controlled. | ✅ Done |
| DIG-02 | As a user, I can bind a digital output to an X-Plane dataref so that the pin state reflects the simulator value. | ✅ Done |
| DIG-03 | As a user, I can specify a dataref array index. | ✅ Done |
| DIG-04 | As a user, I can see the real-time dataref value in the edit form. | ✅ Done |
| DIG-05 | As a user, I can remove a digital output component from the configuration. | ✅ Done |

---

## EPIC 9 — X-Plane Dataref & Command Browser

**As a user, I want to browse and search the full list of X-Plane datarefs and commands so that I can quickly find the right simulator variable for any component.**

| ID | Story | Status |
|----|-------|--------|
| XP-01 | As a user, I can open a dataref browser dialog that lists all X-Plane datarefs with their type, writability, units, and description. | ✅ Done |
| XP-02 | As a user, I can filter datarefs by category so that I can narrow down the list. | ✅ Done |
| XP-03 | As a user, I can search datarefs by name so that I can find a specific variable quickly. | ✅ Done |
| XP-04 | As a user, I can open a command browser dialog that lists all X-Plane commands with their description. | ✅ Done |
| XP-05 | As a user, I can filter commands by category and search by name. | ✅ Done |
| XP-06 | As a user, I can select a dataref or command and have it populated into the relevant field automatically. | ✅ Done |

---

## EPIC 10 — UDP / Networking Configuration

**As a user, I want to configure the UDP connection between this application and X-Plane so that data is exchanged correctly over the network.**

| ID | Story | Status |
|----|-------|--------|
| UDP-01 | As a user, I can configure the local machine IP address and port so that the application listens on the correct interface. | ✅ Done |
| UDP-02 | As a user, I can configure the X-Plane machine IP address and port so that commands and dataref updates are sent to the right host. | ✅ Done |
| UDP-03 | As a user, I can enable UDP traffic redirection to a third machine (IP + port) so that I can relay data to other tools. | ✅ Done |
| UDP-04 | As a user, I can add multiple forward IP addresses so that data is broadcast to multiple network destinations. | ✅ Done |
| UDP-05 | As a user, I can see the live UDP server status in the dialog and in the main window status bar so that I know whether the connection is active. | ✅ Done |
| UDP-06 | As a user, I can apply UDP settings and have the server restart automatically so that changes take effect immediately without restarting the application. | ✅ Done |

---

## EPIC 11 — Instrument / Graphics Panel

**As a user, I want to create and display graphical instrument panels driven by X-Plane data so that I can visualise simulator state on screen.**

| ID | Story | Status |
|----|-------|--------|
| INS-01 | As a user, I can create an instrument panel and set its pixel dimensions. | ✅ Done |
| INS-02 | As a user, I can add graphical components to an instrument panel, each with a texture file, position, size, layer, and origin point. | ✅ Done |
| INS-03 | As a user, I can configure clip rectangles for instrument components so that only a portion of the texture is rendered. | ✅ Done |
| INS-04 | As a user, I can run/preview an instrument panel from within the application so that I can see it rendered. | ✅ Done |
| INS-05 | As a user, I can configure instrument display settings via the graphics config file so that rendering behaviour is persistent. | ⚠️ Partial |
| INS-06 | As a user, I can bind instrument components to X-Plane datarefs so that the display updates in real-time with simulator data. | 🔲 Planned |

---

## EPIC 12 — Application & Logging

**As a user, I want the application to provide feedback and diagnostics so that I can understand what is happening at runtime.**

| ID | Story | Status |
|----|-------|--------|
| LOG-01 | As a user, I can see a live log message table at the bottom of the application so that I can monitor activity and diagnose issues. | ✅ Done |
| LOG-02 | As a user, logging is written to a file (pyXPArduino.log) so that I can review past sessions. | ✅ Done |
| LOG-03 | As a user, log verbosity is configurable per-module via logging_conf.json so that I can control detail level. | ✅ Done |
| LOG-04 | As a user, connection status indicators are colour-coded in the UI so that I can see at a glance what is connected. | ✅ Done |

---

## Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ Done | Implemented and working |
| ⚠️ Partial | Partially implemented |
| 🔲 Planned | Not yet implemented |
| ❌ Removed | Was removed from scope |

---

## Known Defects (tracked separately from stories)

| ID | Description | Severity | File |
|----|-------------|----------|------|
| BUG-01 | `arduinoReady` state not reset on disconnect (assignment vs comparison) | Critical | lib/arduinoSerial.py:237 |
| BUG-02 | Malformed XPath causes IndexError crash when updating a component | Critical | lib/arduinoXMLconfig.py:371 |
| BUG-03 | Silent `except: pass` swallows all serial output failures | High | lib/Arduino.py:144 |
| BUG-04 | Multiple bare `except:` clauses mask errors across modules | High | Multiple |
