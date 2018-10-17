# HEXBUG-Tarantula
This project showcases only the parts where commands were being sent to the HEXBUG Tarantula to move it forward, backwards and to turn right or left.

### Using Arduino UNO to Connect to HEXBUG Controller
The arduino folder contains code used to program an Arduino board soldered to the HEXBUG Tarantula's IR Controller. By wiring to the metal contact plates in the controller, the Arduino board can directly push commands to the Tarantula.

### Using the ESP8266 WiFi Board to Connect to HEXBUG
After successfully linking to the Infrared Remote Control, the HEXBUG Tarantula itself was pulled apart and resoldered to an ESP8266 WiFI Board. The IR Receiver was removed and the board was mounted to it. The goal was to use the WiFi board and communicate with the Tarantula using only python scripts. To do this I programmed using a library called PySerial to communicate through the Arduino's serial port. 
