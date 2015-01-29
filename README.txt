This is the repository for Jason Radcliffe's senior project.

Premise: This project uses a Raspberry pi and an ultrasonic distance sensor
to create an alarm clock that turns off when the user gets out of bed. The
sensor is placed on the ceiling pointing straight down and after being trained
to know the normal distance between itself and the empty bed, it can then
recognize any time when it gets a lower reading, meaning the person is still
in bed.

Equipment used:
1 Raspberry Pi B+
1 Maxbotix ultrasonic rangefinder LV-EZ1
USB wifi adapter (for system time as well as future interfacing with app)
lots of 200 mm male to female jumper wires
3 minigrabbers

Explanation of files:


Alarm-0.1.py  - The first alpha version of the Alarm program. Features command
                  line entering of a target time. Distance is shown on the screen
                  but not used for shutting off the alarm. Sound is played through
                  the HDMI monitor interface.

sensortest.py - A sample program for how the pi measures distances

musictest.py -  A sample program showing how the program plays sounds

topnotch.wav -  A low fidelity copy of a song to be used as an alarm tone

vlc.py      -   Necessary inclusion for the vlc python module to be able to
                   play sounds
