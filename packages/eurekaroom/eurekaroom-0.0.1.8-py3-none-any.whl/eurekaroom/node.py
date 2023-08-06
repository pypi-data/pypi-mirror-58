#import app08t
#import app10t

#from .video import Player
from .video import Player
import tkinter as Tk
import os
import sys
import logging
logger = logging.getLogger(__name__)
from eurekaroom import args
from .tkcontrol import Window
from .gui import GUI

# For Image display
from PIL import Image, ImageTk
from os.path import expanduser


NODE_STATUS_QUICK = 0
NODE_STATUS_NORMAL = 1
NODE_STATUS_DETAILED = 2
NODE_STATUS = {
    'QUICK': NODE_STATUS_QUICK,
    'NORMAL': NODE_STATUS_NORMAL,
    'DETAILED': NODE_STATUS_DETAILED,
}


class EurekaNode():
    """
    A class that ties all the room resources and nodes together and provides access through the API
    """

    name = None
    display = None
    audio = None
    rotation = 0
    player = None
    window=None

#----------------------------------------------------------------------
    def __init__(self, name, rotation=0):

        self.name = name
        self.rotation = rotation
        

#----------------------------------------------------------------------
    def updateWallpaper(self, imagepath):
        """
        This function sets the wallpaper on the device 

        Paramiter:
            imagepath (str): The path to an image
        """

        imagepath = expanduser(imagepath)
        load = Image.open(imagepath).resize( (int( self.display.winfo_screenwidth()), int(self.display.winfo_screenheight())), Image.ANTIALIAS )
        photo = ImageTk.PhotoImage(load)
        self.window.config(image=photo)
        self.window.image=photo

#----------------------------------------------------------------------
    def initDisplay(self, orientation=0):
        """
        Initializes the display window for visuals. Create the Parent class
        """

        ####TODO: initialize the video with accounting for 'orientation' value
        ####?: 'orientation' value should be passed to playVideo()

        # Set local disply so that remote execution does not confuse the target DISPLAY
        if not 'DISPLAY' in os.environ:
            os.environ['DISPLAY'] = ':0.0'
        logging.debug("os.environ['DISPLAY']={}".format(os.environ['DISPLAY']))

        #self.gui = GUI()
        #
        #self.gui.SetBackgroundImage(image="~/code/eurekaroom/media/Meadow.jpg")
        #self.gui.run()

        # Create the TK-Player window root 
        try:
            self.display = Tk.Tk()
        except Exception as err:
            ####TODO: add better exception handling of display initialization failure
            logging.error(err)
            sys.exit(1)
        
        self.display.configure(bg="black")
        self.display.attributes("-fullscreen", True)
        self.window = Tk.Label(self.display)
        self.window.configure(bg="black")
        #self.updateWallpaper(imagepath="~/code/eurekaroom/media/Meadow.jpg")
        self.window.pack(fill=Tk.BOTH, expand=1)

        self.display.update()
        self.display.mainloop()

#----------------------------------------------------------------------
    def initAudio(self):
        """
        Initializes the audio output stream
        """
        ####TODO: add audio initialization code
        pass

#----------------------------------------------------------------------
    def ClosePlayer(self):
        self.player.IsPlaying()
        self.player.closePlayer()
        self.display.update()

        # Set the close function for the TK-Player window
        #self.display.protocol("WM_DELETE_WINDOW", self.player.Close)

        # Set a callback for 'end of video reached'
        #event_manager = self.player.event_manager()
        #event_manager.event_attach(Player.EventType.MediaPlayerEndReached, self.end_callback)

        # Start the main loop for the window events
        #self.display.mainloop()

#----------------------------------------------------------------------
    def playVideo(self, videopath):
        """
        Set and play a video

        Parameters:
            videopath (string): The video to be played
        """
        self.player = Player(parent=self.window, video=videopath, rotation=self.rotation)
        self.player.Play()
        
#----------------------------------------------------------------------
    def end_callback(self, event):
        print('End of media stream (event %s)' % event.type)
        logging.debug("End of media stream (event {}})".format(event.type))
        sys.exit(0)

#----------------------------------------------------------------------
    def playImage(self, imagepath):
        """
        This function displays an image to the default screen on the device it is running on
        """
        ####TODO: check that the image ixists and is accessible
        pass

#----------------------------------------------------------------------
    def playAudio(self, audiopath):
        """
        This function plays an audio file on the device it is running on
        """
        ####TODO: check that the image ixists and is accessible
        pass

#----------------------------------------------------------------------
    def reset(self):
        """
        Resets the hardware and variable state of this device (not to be considerd a reboot, however)
        """
        pass

#----------------------------------------------------------------------
    def getstatus(self, level=NODE_STATUS_NORMAL):
        """
        The Function to get the status of a node

        Parameters:
            level (custom):
                NODE_STATUS_QUICK 
                NODE_STATUS_NORMAL 
                NODE_STATUS_DETAILED 

        Returns:
            A status of the running 'node' based on the detail 'level' requested
        """
        if level==NODE_STATUS_QUICK:
            status = True
        elif level==NODE_STATUS_NORMAL:
            status = {
                'state': 'running',
                'description':'running with no errors'
            }
        else:
            #### TODO: add complete dynamic status response for the detailed request
            status = {
                'state': 'running',
                'description':'running with no errors',
                'name': self.name,
                # etc...
            }

        return status
