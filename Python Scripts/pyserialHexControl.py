# IMPORT PACKAGES
import numpy as np
import sys
import serial
import time
port = '/dev/cu.SLAB_USBtoUART'
baudrate = 9600

# Connect to Serial Port
ser = serial.Serial(port, baudrate, timeout=None)

# Allow for Arduino Board to startup
time.sleep(2)

# Poll for any responses while the serial port is open
# while (True):
#     if (serial.inWaiting()>0):
while(serial.is_open):
  line = ser.readline()
  if len(line) > 0:
    # parse the input: "F,R,L,B"
    commands = line.split(',')
    for x in commands:
      if x == "F":
        forward()
        time.sleep(2)
      if x == "R":
        turn_right()
        time.sleep(2)
      if x == "L":
        turn_left()
        time.sleep(2)
      if x == "B":
        back()
        time.sleep(2)
      else:
        time.sleep(2)

def forward():
  ser.write(b"W")

def back():
  ser.write(b"S")

def turn_right():
  ser.write(b"D")

def turn_left():
  ser.write(b"A")

def make_square():
  for i in range(4):
    turn_right()
    time.sleep(1)
    forward()
    time.sleep(1)

def zig_zag():
  for i in range(2):
    forward()
    time.sleep(1)
    turn_right()
    time.sleep(1)
    forward()
    time.sleep(1)
    turn_left()
    time.sleep(1)

# make_square()
# zig_zag()

