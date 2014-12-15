This is the repository for Jason Radcliffe's senior project.

Premise: This project uses a Raspberry pi and an ultrasonic distance sensor to create an alarm clock
that turns off when the user gets out of bed. The sensor is placed on the ceiling pointing straight
down and after being trained to know the normal distance between itself and the empty bed, it can
then recognize any time when it gets a lower reading, meaning the person is still in bed.

Equipment used:
1 Raspberry Pi B+
1 Maxbotix ultrasonic rangefinder LV-EZ1
USB wifi adapter (for system time as well as future interfacing with app)

Explanation of files:

vlc.py - necessary inclusion for the vlc python module to be able to play sounds

sensortest.py - A sample program for how the pi measures distances

musictest.py - A sample program showing how the program plays sounds

topnotch.wav - a low fidelity copy of a song to be used as an alarm tone