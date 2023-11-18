import threading
import time
import vlc
from tkinter import *

def play():
    volumethread = threading.Thread(target=refreshvolume, daemon=True)
    volumethread.start()

def refreshvolume():
    while True:
        changevolume(volume.get())
        time.sleep(0.1)

def changevolume(volume):
    player.audio_set_volume(volume)
    time.sleep(0.1)

player = vlc.MediaPlayer()
# media = vlc.Media('test.mp3')
# player.set_media(media)
player.set_mrl('test.mp3')
player.audio_set_volume(100)
player.play()

root = Tk()
root.title("Playlist Player")
root.geometry("700x200")

volume = Scale(root, from_=0, to=100, orient=HORIZONTAL)
volume.set(100)
volume.place(x=150, y=20)

play()
root.mainloop()


# clip = MP3('test.mp3')
# clip_info = clip.info
time.sleep(300)  # Wait until after the clip has finished

player.stop()

