import argparse
import logging

#####
# Parse the commandline

class Args(object):
    # Create the commandline parser
    parser = argparse.ArgumentParser()


    def __init__(self, config):

        # Clean the rotation value
        try:
            rotation = float(config.parser['general']['rotation'])
            if rotation > 360.0:
                rotation = 0.0
        except:
            rotation = 0.0
        
        #logging.debug("rotation set to {} - {}".format(rotation, args.rotation))
        
        # Add parser arguments for every flag and parameter.  Leave nothing hard-coded
        self.parser.add_argument("-v", "--verbose", action="store_true", 
            help="increase output verbosity")
        self.parser.add_argument("-e", "--emulategpio", action="store_true", 
            help="use on non-Raspberry Pis to emulate the GPIO access")
        self.parser.add_argument("-n", "--nodename", type=str, default=config.parser["general"]["nodename"],
            help="name (id) of the node node ('{}')".format(config.parser['general']['nodename']))
        self.parser.add_argument("-r", "--rotation", type=float, default=rotation,
            help="set display rotation ('{}')".format(rotation))
        self.parser.add_argument("-p", "--port", type=int, default=config.parser['general']['port'],
            help="port to serve the RESTful API on ({})".format(config.parser['general']['port']))
        self.parser.add_argument("-m", "--mediapath", type=str, default=config.parser['general']['mediapath'],
            help="path to the media directory ({})".format(config.parser['general']['mediapath']))
        self.parser.add_argument("-s", "--servermode", action="store_true",
            help="run as server using specified port")
        self.parser.add_argument("-w", "--writeconfig", action="store_true",
            help="write configuration back to the ini file")
        self.parser.add_argument("-a", "--autoaddmedia", action="store_true",
            help="automatically add all media in mediapath ({})".format(config.parser['general']['mediapath']))
        self.parser.add_argument("--installservice", action="store_true",
            help="NOTE: For Production systems only!!! Installs systemd-service to run server at boot time")

    def parsArgs(self):
        return self.parser.parse_args()
