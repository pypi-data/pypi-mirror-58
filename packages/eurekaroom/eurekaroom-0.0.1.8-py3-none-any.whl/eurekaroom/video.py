#!/usr/bin/env python3

# Tested with Python 3.7.4, tkinter/Tk 8.6.9 on macOS 10.13.6 only.
__version__ = '19.07.29'  # mrJean1 at Gmail dot com

# import external libraries
import vlc
# import standard libraries
import tkinter as Tk
from tkinter import ttk
from os.path import expanduser, isfile
from time import sleep

# For Image display
from PIL import Image, ImageTk

#----------------------------------------------------------------------
class Player(Tk.Frame):
    """
    The window that deals with videos.
    """

#----------------------------------------------------------------------
    def __init__(self, parent, video, rotation=0.0, title=None):
        """
        Constructor for the Player class

        Parameters:
            parent (TK class): The root container
            video (str): The path leading to the video
            rotation (float): The amount the video should be rotated
        """

        self.parent = parent  # == root
        
        self.video = expanduser(video)
        self.rotation = rotation

        # video panel
        self.videopanel = ttk.Frame(self.parent)
        self.canvas = Tk.Canvas(self.videopanel, bg="black")
        
        self.canvas.pack(fill=Tk.BOTH, expand=1)
        self.videopanel.pack(fill=Tk.BOTH, expand=1)
        
        self.volMuted = False

        # VLC player
        args = []
        args.append('--no-xlib')
        args.append('--quiet')
        if rotation > 0.0:
            args.append("--rotate-angle={}".format(rotation))
            args.append('--video-filter=rotate')
        print("=========== Video args: {}".format(args))
        self.Instance = vlc.Instance(args)
        self.player = self.Instance.media_player_new()

#----------------------------------------------------------------------
    def IsPlaying(self):
        """
        Checks if the Video is still playing
        """
        sleep(1)
        while self.player.is_playing():
            sleep(1)

#----------------------------------------------------------------------
    def closePlayer(self, *unused):
        """
        Closes, the VLC Instance and Frame
        """

        ####* Shutdown the VLC Player
        self.player.stop()
        self.player.release()
        self.Instance.release()

        ####* Shutdown the Video Frame
        self.videopanel.destroy()
        
#----------------------------------------------------------------------
    def Play(self):

        ####* Ensures that a valid video file is specified, then load and play it
        if isfile(self.video):
            m = self.Instance.media_new(str(self.video))
            self.player.set_media(m)

            ####* set the window id where to render VLC's video output
            h = self.videopanel.winfo_id()  # .winfo_visualid()?
            self.player.set_xwindow(h)  # fails on Windows
            self.player.play()

#----------------------------------------------------------------------    
    def show(self):
        """
        Displays an Image
        
        #! Currently not in use 12-26-2019
        """
        if isfile(self.video):
            load = Image.open(self.video).resize((int(self.canvas.winfo_width()), int(self.canvas.winfo_height()) ))
            render = ImageTk.PhotoImage(load)
            
            img = Tk.Label(self.canvas, image=render)
            img.image = render
            img.pack(fill=Tk.BOTH, expand=1)
            img.place(x=0, y=0)
            #self.parent.update()