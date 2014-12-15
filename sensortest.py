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
 distance1=measure()
 time.sleep(0.1)

 distance2=measure()
 time.sleep(0.1)

 distance3=measure()
 time.sleep(0.1)

 distance = distance1 + distance2 + distance3

 distance = distance / 3

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
  while True:
   distance = measure_avg()
   if distance != 800:
    break
  print "Distance: %.1f cm" % distance
  time.sleep(1)
except KeyboardInterrupt:
 GPIO.cleanup()






























