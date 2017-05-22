#!/usr/bin/env python3
"""
  Turns on an LED on for one second, then off for one second, repeatedly.
  Most Arduinos have an on-board LED you can control. On the Uno and
  Leonardo, it is attached to digital pin 13. If you're unsure what
  pin the on-board LED is connected to on your Arduino model, check
  the documentation at http://www.arduino.cc
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

BOARD_LED = 13
COM_PORT = None
board = PyMata3(com_port=COM_PORT)

# SET PIN VALUES TO GLOBAL VARIABLES 'LOW' & 'HIGH'
LOW = 0
HIGH = 1

# INITIALIZE GROUND, POWER, AND CONTROLLER PINS
PIN_GROUND = 7        #A0
PIN_VPOW = 6          #A1
# MOVE FORWARD
TURN_RIGHT = 5        #A2
TURN_LEFT = 3         #A4
# MOVE BACKWARDS
TURN_LEFT_BACK = 4    #A3
TURN_RIGHT_BACK = 2   #A5

commands = [1,2,3,4]

lastCommand_millis = 0
commandDuration_millis = 500


PIN_MODE = 0  # This is the PyMata Pin MODE = ANALOG = 2 and DIGITAL = 0x20:
PIN_NUMBER = 1
DATA_VALUE = 2

def setup():
    # Testing Arduino LED
    board.set_pin_mode(BOARD_LED, Constants.OUTPUT)

    # INITIALIZE GROUND PIN
    board.set_pin_mode(PIN_GROUND, Constants.OUTPUT)
    board.digital_write(PIN_GROUND, LOW)
    print("This is the ground pin:")
    print(board.get_pin_state(PIN_GROUND))

    # INITIALIZE POWER SOURCE PIN
    board.set_pin_mode(PIN_VPOW, Constants.OUTPUT)
    board.digital_write(PIN_VPOW, HIGH)
    print("This is the power pin:")
    print(board.get_pin_state(PIN_VPOW))

    # INITIALIZE THE REST OF THE PINS
    stop()

def stop():
    print("Inside STOP")
    # out = 1, input = 0, analog=2,
    board.set_pin_mode(TURN_RIGHT, Constants.INPUT)
    board.digital_write(TURN_RIGHT, LOW)

    board.set_pin_mode(TURN_LEFT_BACK, Constants.INPUT)
    board.digital_write(TURN_LEFT_BACK, LOW)

    board.set_pin_mode(TURN_LEFT, Constants.INPUT)
    board.digital_write(TURN_LEFT, LOW)

    board.set_pin_mode(TURN_RIGHT_BACK, Constants.INPUT)
    board.digital_write(TURN_RIGHT_BACK, LOW)

    print("Finishing Stop")
    print(board.get_pin_state(TURN_RIGHT))
    print(board.get_pin_state(TURN_LEFT))
    # print(board.get_pin_state(TURN_RIGHT_BACK))
    # print(board.get_pin_state(TURN_LEFT_BACK))

def move_forward():
    board.set_pin_mode(TURN_RIGHT, Constants.OUTPUT)
    board.digital_write(TURN_RIGHT, LOW)
    board.set_pin_mode(TURN_LEFT, Constants.OUTPUT)
    board.digital_write(TURN_LEFT, LOW)

    print("Inside Move Forward")
    print(board.get_pin_state(TURN_RIGHT))
    print(board.get_pin_state(TURN_LEFT))

def move_backward():
    board.set_pin_mode(TURN_RIGHT_BACK, Constants.OUTPUT)
    board.digital_write(TURN_RIGHT_BACK, LOW)
    board.set_pin_mode(TURN_LEFT_BACK, Constants.OUTPUT)
    board.digital_write(TURN_LEFT_BACK, LOW)

def turn_clock():
    print("Inside turn_clock")
    board.set_pin_mode(TURN_RIGHT_BACK, Constants.OUTPUT)
    board.digital_write(TURN_RIGHT_BACK, LOW)
    board.set_pin_mode(TURN_RIGHT, Constants.OUTPUT)
    board.digital_write(TURN_RIGHT, LOW)
    print("Finishing Turn Clock")
    print(board.get_pin_state(TURN_RIGHT))
    print(board.get_pin_state(TURN_RIGHT_BACK))

def turn_cclock():
    board.set_pin_mode(TURN_LEFT_BACK, Constants.OUTPUT)
    board.digital_write(TURN_LEFT_BACK, LOW)
    board.set_pin_mode(TURN_LEFT, Constants.OUTPUT)
    board.digital_write(TURN_LEFT, LOW)

def loop():
    print("STOP")
    board.digital_write(BOARD_LED, 0)
    stop()
    board.sleep(2)
    print("TURN CLOCK")
    board.digital_write(BOARD_LED, 1)
    turn_cclock()
    board.sleep(2)


def main():
  print("Setup")
  setup()
  while True:
      loop()

if __name__ == "__main__":
   main()