#!/usr/bin/python

# Get number of seconds the ARMinARM board is powered from the RTC
# read /dev/ttyAMA0 @ 9600 baud

# The firmware on the STM32 spits out a 32 bit binary number every second as a string
# So reading the line can take up to a second
# If you're unlucky and run the script halfway receiving the number, this script will fail

import time
import serial

def read_rtc():
  ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    xonxoff=0, rtscts=0, dsrdtr=0,
    timeout = 1200,
  )
  ser.isOpen()
  result = "" + ser.readline()
  ser.close()
  return result

binaryline = read_rtc().strip()
seconds = int(binaryline, 2)

print binaryline
print "" + `seconds` + " seconds"
print "= " + `(seconds / 60.0)` + " minutes"
print "= " + `(seconds / 60.0 / 60.0)` + " hours"
print "= " + `(seconds / 60.0 / 60.0 / 24.0)` + " days"
