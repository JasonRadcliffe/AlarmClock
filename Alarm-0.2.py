#Alarm-0.2.py
#Author: Jason Radcliffe  -  February 2015
#modified from code from Matt Hawkins and Bob Tidey

import time
import RPi.GPIO as GPIO
import vlc
import os

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


#this function takes an Hour [1-12], a minute, and a boolean pm
# value and returns a 9 value time tuple for the next time the
# given input will occur.
def getWakeTuple(wakeHour, wakeMin, wakeIsPM):

#convert from regular to military time
 if wakeHour == 12:
  if wakeIsPM == False:   
   wakeHour = 0
 elif wakeIsPM == True:
   wakeHour +=12

#get current time and figure out if the alarm is for today or tomorrow
 curTime = time.localtime(time.time())

 isToday = False
 if wakeHour > curTime[3]:   
  isToday = True
 elif wakeHour == curTime[3] and wakeMinute > curTime[4]:
  isToday = True
 

 
 if isToday == True:
  wakeTuple = (curTime[0], curTime[1], curTime[2], wakeHour, wakeMinute, curTime[5], curTime[6], curTime[7], curTime[8])
  return wakeTuple

 if isToday == False:
  secondsTillTomorrow = (3600 * (23 - curTime[3]) ) + (60 * (60 - curTime[4]))
  tomorrowTuple = time.localtime(time.time() + secondsTillTomorrow)
  secondsTillWake = (3600 * wakeHour) + (60 * wakeMinute)
  wakeTuple = time.localtime(time.mktime(tomorrowTuple) + secondsTillWake)
  return wakeTuple 
  
  

#-----------------------------------------------------------------------
#main
#--------------------------------------------------------------------------

player = vlc.MediaPlayer("topnotch.wav")
GPIO.setmode(GPIO.BCM)

trig = 23

GPIO.setup(trig, GPIO.OUT)
GPIO.output(trig, False)

#try block to listen for user pressing CTRL-C
try:

 #rudimentary method of obtaining wake time
 wakeHour= input('What hour do you want to get up?')
 wakeMinute = input('What minute do you want to get up?')
 wakePM= input('PM? (True or False)')
 #print time.asctime(wakeTuple)
 #print time.asctime(time.localtime(time.time()))
 
 wakeTuple = getWakeTuple(wakeHour, wakeMinute, wakePM)
 print "Alarm is set for:", time.asctime(wakeTuple)
 secondsTillWake = time.mktime(wakeTuple) - time.time()
 print secondsTillWake, " seconds until the alarm rings!"
 time.sleep(secondsTillWake)
 player.play()
 bedEmptyStrikes = 0

#initial bed check method using magic number of 96 cm
 while bedEmptyStrikes <= 3:
  distance = measure_avg()
  if (distance >= 96.5):
   print "Looks like you're up! Distance: %.1f cm" % distance
   bedEmptyStrikes+=1

  else:
   print "Looks like you're still in bed. Distance: %.1f cm" % distance
   if bedEmptyStrikes > 0:
    bedEmptyStrikes -=1
   time.sleep(1)
 
 player.pause()
except KeyboardInterrupt:
 GPIO.cleanup()
 os.remove('vlc.pyc')






























