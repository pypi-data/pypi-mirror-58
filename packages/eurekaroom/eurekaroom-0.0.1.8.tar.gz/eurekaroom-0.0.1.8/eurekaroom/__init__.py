#####
# Setup and initialization

# Load our initial libraries and tools
from .config import config
from .args import Args
from .node import EurekaNode
from .video import Player
import logging
from .createService import InstallService

parsing = Args(config)
args = parsing.parsArgs()

mynode = EurekaNode(name=args.nodename)
logging.info("Created node '{}'".format(args.nodename))


#####
# Media
# Check for media config section
if args.autoaddmedia:
    config.checkMedia(args)
#
#####

if args.writeconfig:
    config.storeConfig(args)

if args.servermode:
    from flask import Flask

    # Initialize the Flask service object
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'you-will-never-guess'

    from eurekaroom import routes

if args.installservice:
    InstallService()