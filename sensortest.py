#sensortest.py
#Author: Jason Radcliffe  -  October 2014
#modified from code from Matt Hawkins and Bob Tidey

import time
import RPi.GPIO as GPIO

#function that pulses the trigger and receives a measurement
def measure():

 #put high voltage on trigger line for .00001 seconds
 GPIO.output(trig, True)
 time.sleep(0.00001)
 GPIO.output(trig, False)

 start = time.time()

 #change the GPIO line to be an input
 GPIO.setup(trig, GPIO.IN)



 #start gets reset until it hears a 1 from TRIGECHO
 while GPIO.input(trig)==0:
  start=time.time()
 

 #stop gets pushed out until it starts hearing 0 again from TRIGECHO
 while GPIO.input(trig)==1:
  stop=time.time()

 #change GPIO back to an output
 GPIO.setup(trig, GPIO.OUT)

 GPIO.output(trig, False)

 elapsed = stop-start
 distance = (elapsed * 34300)/2.0
 return distance


def measure_avg():
 valid1 = False
 valid2 = False
 valid3 = False

 while True:
  
  if valid1 != True:
   distance1=measure()
   valid1 = True
   time.sleep(0.1)
  
  if valid2 != True:
   distance2=measure()
   valid2 = True
   time.sleep(0.1)

  if valid3 != True:
   distance3=measure()
   valid3 = True
   time.sleep(0.1)

  distance = distance1 + distance2 + distance3

  distance = distance / 3
  
  if abs(distance1 - distance2) > 3:
   if abs(distance1 - distance3) > 3:
    valid1 = False
   else:
    valid2 = False
  
  if abs(distance1 - distance3) > 3:
   valid3 = False
  
  if (valid1 and valid2 and valid3):
   break
 return distance


#-----------------------------------------------------------------------
#main
#--------------------------------------------------------------------------

GPIO.setmode(GPIO.BCM)

trig = 23
print "Here is the Ultrasonic Measurements"

GPIO.setup(trig, GPIO.OUT)
GPIO.output(trig, False)

#try block to listen for user pressing CTRL-C
try:
 while True:
  distance = measure_avg()
  print "Distance: %.1f cm" % distance
  time.sleep(1)
except KeyboardInterrupt:
 GPIO.cleanup()






























