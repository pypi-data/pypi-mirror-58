import tkinter as Tk

# For Image display
from PIL import Image, ImageTk
from os.path import expanduser

class GUI(object):

    def __init__(self):
        self.root = Tk.Tk()
        self.root.configure(bg="black")
        self.root.attributes("-fullscreen", True)
        self.root.update()
    
    def run(self):
        
        self.root.mainloop()
    
    def Label(self, parent):
        label = Tk.Label(parent)
        return label

    #----------------------------------------------------------------------
    def updateWallpaper(self, size, imagepath):
        """
        This function sets the wallpaper on the device 

        Paramiter:
            imagepath (str): The path to an image
        """

        imagepath = expanduser(imagepath)
        load = Image.open(imagepath).resize( size, Image.ANTIALIAS )
        photo = ImageTk.PhotoImage(load)

        return photo
    
    def SetBackgroundImage(self, image):
        """
        The function that sets the background image of the root window.

        Paramaters:
            image(str): the path to the image.

        """
        self.background = Tk.Label(self.root)
        
        photo = self.updateWallpaper(size = (int( self.root.winfo_screenwidth()), int(self.root.winfo_screenheight())), imagepath=image )
        
        self.background.config(image=photo)
    
        self.background.image=photo
        self.background.pack(fill=Tk.BOTH, expand=1)
        
        self.root.update()
    