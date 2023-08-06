import configparser
import logging
import socket
import os
import sys
from pathlib import Path


# Used to check file types
from magic import from_file

#####
# Load or create cofig from config.ini

# Load any stored values from our last run to use as defaults, create entries if the are not there.
class Config(object):

    parser = None

    def __init__(self):
        self.home = str(Path.home())
        self.configDir = os.path.join(self.home,".config","eurekaroom",)

        self.parser = configparser.ConfigParser()
        self.parser['general'] = {
            'port': '5000', 
            'mediapath': 'media/',
            'nodename': socket.gethostname(),
            'configpath': self.configDir
            }
        
        ####TODO: validate or create the config.ini file, here
        try:
            os.mkdir(path= self.configDir)
        except Exception as error:
            logging.debug('Error making dir with exception {}'.format(error))
        finally:
            logging.debug('Created dir at {}'.format(self.configDir))
        
        self.configfile = os.path.join(self.configDir,"config.ini")
        self.parser.read(self.configfile)
        logging.debug('Configuration read in')

    def checkMedia(self, args):

        if not self.parser.has_section('media'):
            self.parser.add_section('media')
            logging.info("No 'media' section was been defined yet. An empty section has been added.  Use -a to auto-populate it.")

            # If this is an empty config, and the media has not yet been added, but -a flag is set,
            # automatically scan the specified media folder and add the files to the config    
           
        logging.debug("Automatically adding the media files from {}".format(args.mediapath))
        for dirpath, dirnames, files in os.walk(args.mediapath):
            logging.debug('Found directory: {}'.format(dirpath))
            for file_name in files:
                logging.debug("Adding media to config {}/{}".format(dirpath, file_name))      
                # strip out any non media files as we go 
                type = from_file(dirpath + '/' + file_name, mime=True)
                type = str(type)[0:type.find('/')]
                if type.startswith(tuple(['video', 'image', 'audio'])):   
                    self.parser.set('media', file_name, "{}/{}".format(dirpath, file_name))      
    
    #def getconfig(self):
    #    return self.config
    
    #####
    #
    # Store the configuration changes from arguments back to the ini file for next time
    def storeConfig(self, args):

        self.parser['general']['port'] = "{}".format(args.port)
        self.parser['general']['mediapath'] = "{}".format(args.mediapath)
        self.parser['general']['nodename'] = "{}".format(args.nodename)
        with open(self.configfile, 'w') as configfile:
            self.parser.write(configfile)
        sys.exit()
    #
    #####
######
## Load or create config from config.ini
config = Config()
logging.debug("Config set to {}".format(config.parser["general"]["port"]))
#
#####

