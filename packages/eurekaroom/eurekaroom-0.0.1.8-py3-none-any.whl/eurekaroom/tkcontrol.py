import sys
import tkinter as Tk
# from tkinter import ttk

# For Image display
from PIL import Image, ImageTk
from os import path

########################################################################
class OtherFrame(Tk.Toplevel):
    """"""
 
#----------------------------------------------------------------------
    def __init__(self, original):
        """Constructor"""
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        #self.geometry("400x300")
        #self.title("otherFrame")
 
        #btn = Tk.Button(self, text="Close", command=self.onClose)
        #btn.pack()
 
#----------------------------------------------------------------------
    def onClose(self):
        """"""
        self.destroy()
        self.original_frame.show()
 
########################################################################


class Window(Tk.Frame):
    """The main window has to deal with events.
    """
    background=None

#----------------------------------------------------------------------
    def __init__(self, parent, rotation=0.0, title=None):
       

        self.parent = parent  # == root
        self.parent.title(title or "tkVLCplayer")

        self.frame= Tk.Frame(parent)
        self.frame.pack()

        # Set fullscreen to true
        self.parent.attributes("-fullscreen", True)

        self.parent.update()
        self.parent.mainloop()

#----------------------------------------------------------------------
    def Close(self, *unused):
        ### Closes the window and quit.

        self.parent.quit()  # stops mainloop
        self.parent.destroy()  # this is necessary on Windows to avoid
        # ... Fatal Python Error: PyEval_RestoreThread: NULL tstate
        sys.exit(0)
    
#----------------------------------------------------------------------
    def hide(self):
        self.parent.withdraw()
 
#----------------------------------------------------------------------    
    def openFrame(self):
        self.hide()
        subFrame = OtherFrame(self)

#----------------------------------------------------------------------
    def show(self):
        """"""
        self.parent.update()
        self.parent.deiconify()
 
#----------------------------------------------------------------------
    def setbackground(self, imagepath=None):
        """
        This function the current wallpaper on the device it is running on

        # * Experimental
        """
        subFrame = OtherFrame(self)

        imagepath = path.expanduser(imagepath)
        ##if path.isfile(imagepath):
        load = Image.open(imagepath)#(int(self.parent.winfo_width()), int(self.parent.winfo_height()) ))
        render = ImageTk.PhotoImage(load)
        self.background = Tk.Label(subFrame, image=render)
        self.background.image = render
        self.background.pack(fill=Tk.BOTH, expand=1)
        self.background.place(x=0, y=0)
        self.parent.update()