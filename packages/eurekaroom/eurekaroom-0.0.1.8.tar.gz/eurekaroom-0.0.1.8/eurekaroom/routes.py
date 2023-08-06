from eurekaroom import app
# Import the flask library
from flask import render_template, flash, redirect, url_for
from threading import Thread
from .general import PlayandClose, checkMedia, SetMediaPath,setBackground, createNode
from eurekaroom import config, args

# The Node identifier tells us weather or not a TK frame has been created.
Node=False

#----------------------------------------------------------------------
# Create a default route
@app.route('/')
@app.route('/index/')
def index():
    """
    Display Main/Index page
    """

    media = dict(config.parser.items('media'))
    return render_template('index.html', title="Eurekaroom", name=args.nodename, media=media, node=Node)

#----------------------------------------------------------------------
@app.route("/ListMedia/")
def ListMedia():
    """
    This function renders a list of available media on the current node
    """
    media = dict(config.parser.items('media'))
    return render_template('listmedia.html', title="Eurekaroom", name=args.nodename, media=media)

#----------------------------------------------------------------------
# Plays a specified video by ID (from config.ini:media:{})
@app.route("/PlayVideo/<VideoID>/")
def Video(VideoID):
    """
    This function plays a video.

    Paramater:
        VideoID (str): the name of the desired video
    
    Returns:
        To the home/Index page
    """
    
    media = dict(config.parser.items('media'))

    if checkMedia(VideoID, config):
        media = SetMediaPath(VideoID, config)
        Thread(target=PlayandClose, args=(app, media)).start()
        flash('Now Playing, "{}", on node "{}"'.format(VideoID, args.nodename))
    else:
        flash('Could not find, "{}", on node "{}"'.format(VideoID, args.nodename))

    return redirect(url_for('.index'))

#----------------------------------------------------------------------
@app.route("/DisplayPicture/<PictureID>")
def DisplayPicture(PictureID):
    pass
    #media_file = SetMediaPath(type = 'Pictures', file = media['MEDIA'][PictureNumber])

#----------------------------------------------------------------------
@app.route("/CreateNode/")
def activateNode():
    """
    Creates the Root Window for the desired node.
    """

    Thread(target= createNode).start()
    global Node 
    Node = True
    flash('Window created on node "{}"'.format(args.nodename))

    return redirect(url_for('.index'))
    
#----------------------------------------------------------------------
@app.route("/SetBackground")
def listBackgrounds():
    media = dict(config.parser.items('media'))
    return render_template('backgrounds.html', title="Eurekaroom", name=args.nodename, media=media)

#----------------------------------------------------------------------
@app.route("/SetBackground/<PictureID>")
def SetBackground(PictureID):
    """
    The function that sets the background for the main window.

    Paramater:
        PictureID (str): The name of the image to set as background.
    """
    
    media = dict(config.parser.items('media'))
    
    if checkMedia(PictureID, config):
        mediapath = SetMediaPath(PictureID, config)
        setBackground(mediapath)

    flash('Background set to: "{}"'.format(PictureID))
    return redirect(url_for('.index'))