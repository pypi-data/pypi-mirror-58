import logging

from eurekaroom import EurekaNode, args, mynode

# General Functions

#----------------------------------------------------------------------
# * Initialize the Root Tk Display 
def createNode():

    mynode.initDisplay()
    logging.info("Initialized '{}' display window".format(args.nodename))

#----------------------------------------------------------------------
def PlayandClose(app, mediapath):
    with app.app_context():
        playing_video = PlayVideo(mediapath)
        playing_video.ClosePlayer()

#----------------------------------------------------------------------
def PlayVideo(path):

    ####TODO:  validate that the videoid target actually exists before attemptint load it   
      
    mynode.playVideo(videopath=path)
    logging.info("Played '{}'".format(path))

    return mynode

#----------------------------------------------------------------------
def SetMediaPath(mediaID, config):

    ####TODO: validate that the MediaID also exists, and take action if it is not
    
    media = dict(config.parser.items('media'))[mediaID]
    
    return media

#----------------------------------------------------------------------
def checkMedia(mediaID, config):
    return config.parser.has_option('media', mediaID)

#----------------------------------------------------------------------
def setBackground(mediaID):

    mynode.updateWallpaper(imagepath=mediaID)