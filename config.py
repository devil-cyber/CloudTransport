import sys
import os
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from configparser import ConfigParser
from colored import fg, bg, attr
from pathlib import Path
home = str(Path.home())
config_path = home +  "/.cloudtransport/config.ini"
path_history = home + "/.cloudtransport/history.txt"


class Config:
    def __init__(self):
        pass
    
    def set_config():
        config_object = ConfigParser()
        print ('%s%s Provide details for remote server configuration!!! %s' % (fg('orchid'), attr('bold'), attr('reset')))
        hostname = prompt('Give hostname:', history=FileHistory(path_history))
        path = prompt('Give private key path:', history=FileHistory(path_history))
        port = prompt('Give port (mainly it is 22):', history=FileHistory(path_history))
        username = prompt('Give username (remote server name):', history=FileHistory(path_history))
        config_object["SERVERINFO"] = {
            "hostname": hostname,
            "port": port,
            "path": path,
            "username" : username,
            }
        with open(config_path, 'w') as conf:
            config_object.write(conf)
            try:
                config_object.read(config_path)
                server_info=config_object['SERVERINFO']
                hostname = server_info['hostname']
                port = server_info['port']
                username = server_info['username']
                path = server_info['path']
            except Exception as e:
                print ('%s%s Configuration Unccessfull! Try Again %s' % (fg('red'), attr('bold'), attr('reset')))
                sys.exit()
        print ('%s%s Configuration Created Successfully!!! %s' % (fg('green'), attr('bold'), attr('reset')))
        