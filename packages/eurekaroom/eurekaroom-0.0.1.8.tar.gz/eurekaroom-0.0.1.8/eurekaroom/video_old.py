#!/usr/bin/env python3

# Tested with Python 3.7.4, tkinter/Tk 8.6.9 on macOS 10.13.6 only.
__version__ = '19.07.29'  # mrJean1 at Gmail dot com

# import external libraries
import vlc
# import standard libraries
import sys
import tkinter as Tk
from tkinter import ttk
from os.path import basename, expanduser, isfile
from pathlib import Path
from time import sleep

# For Image display
from PIL import Image, ImageTk


class Player(Tk.Frame):
    """The main window has to deal with events.
    """

    def __init__(self, parent, video, rotation=0.0, title=None):
        Tk.Frame.__init__(self, parent)

        self.parent = parent  # == root
        self.parent.title(title or "tkVLCplayer")
        self.video = expanduser(video)
        self.rotation = rotation

        

        # video panel
        self.videopanel = ttk.Frame(self.parent)
        self.canvas = Tk.Canvas(self.videopanel)
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

        # Set fullscreen to true
        self.parent.attributes("-fullscreen", True)

        self.parent.update()

    def Close(self, *unused):
        """Closes the window and quit.
        """
        # print("_quit: bye")
        self.parent.quit()  # stops mainloop
        self.parent.destroy()  # this is necessary on Windows to avoid
        # ... Fatal Python Error: PyEval_RestoreThread: NULL tstate
        sys.exit(0)

    def closePlayer(self, *unused):
        self.player.stop()
        self.player.release()
        self.Instance.release()

    def Play(self):

        # Ensure that a valid video file is specified and load it, then play it
        if isfile(self.video):  # Creation
            m = self.Instance.media_new(str(self.video))  # Path, unicode
            self.player.set_media(m)
            self.parent.title("tkVLCplayer - %s" % (basename(self.video),))

            # set the window id where to render VLC's video output
            h = self.videopanel.winfo_id()  # .winfo_visualid()?
            self.player.set_xwindow(h)  # fails on Windows
            self.player.play()
    
    def show(self):
        if isfile(self.video):
            load = Image.open(self.video).resize((int(self.canvas.winfo_width()), int(self.canvas.winfo_height()) ))
            render = ImageTk.PhotoImage(load)
            #self.parent.create_bitmap(background=render)
            img = Tk.Label(self.canvas, image=render)
            img.image = render
            img.pack(fill=Tk.BOTH, expand=1)
            img.place(x=0, y=0)
            #self.parent.update()

           

    def IsPlaying(self):
        sleep(1)
        while self.player.is_playing():
            sleep(1)
        
##############################
# This is just for testing and will be removed before final code RC
####TODO: remove this section before final RC
if __name__ == "__main__":

    _video = ''

    while len(sys.argv) > 1:
        arg = sys.argv.pop(1)
        if arg:  # video file
            _video = expanduser(arg)
            if not isfile(_video):
                print('%s error: no such file: %r' % (sys.argv[0], arg))
                sys.exit(1)

    # Create a Tk.App() to handle the windowing event loop
    root = Tk.Tk()
    player = Player(root, video=_video)
    player.show()
    root.protocol("WM_DELETE_WINDOW", player.Close)
    root.mainloop()
    