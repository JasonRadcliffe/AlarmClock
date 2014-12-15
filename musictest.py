#trying with the VLC module

import time
import vlc
player = vlc.MediaPlayer("topnotch.wav")
player.play()
time.sleep(5)
print("success!")


