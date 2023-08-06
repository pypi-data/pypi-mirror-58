import systemd_unit
from elevate import elevate
from os import geteuid, path

def InstallService():
    
    current_dir_path = path.dirname(path.realpath(__file__))
    service_script_path = path.join(current_dir_path, 'installScripts', 'eurekaroom.service')
    f=open(service_script_path, "r")
    content = f.read()
    f.close()
    myservice = systemd_unit.Unit(name = "eurekaroom", content= content)
    
    # TODO: Make this check for sudo su
    elevate()
    if geteuid() == 0:
        myservice.ensure()
    else:
        print("Please install eureakaroom under root.")
