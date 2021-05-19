import sys
import os
import paramiko
import itertools
import threading
import time
from configparser import ConfigParser
from config import Config
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from colored import fg, bg, attr
from pathlib import Path

home = str(Path.home())
config_path = home + "/.cloudtransport/config.ini"

config_object = ConfigParser()


class Authorize:
    def auth():
        done = False

        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\r Connecting ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
        try:
            config_object.read(config_path)
            server_info = config_object['SERVERINFO']
            hostname = server_info['hostname']
            port = server_info['port']
            username = server_info['username']
            path = server_info['path']
        except Exception as e:
            print(str(e))
            print('Set config file correctly')
            sys.exit()
        try:
            key = paramiko.RSAKey.from_private_key_file(path)
        except paramiko.PasswordRequiredException:
            passw = input('Provide private key encyraption password:')
            print()
            key = paramiko.RSAKey.from_private_key_file(path, password=passw)
        except FileNotFoundError as e:
            print(str(e))
            print('Set config file correctly')
            sys.exit()
        except Exception as e:
            print(str(e))
            print('Set config file correctly')
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            t = threading.Thread(target=animate)
            t.start()
            client.connect(hostname=hostname, username=username, pkey=key)
            done = True
            print('%s%s Connected Successfully!!! %s' %
                  (fg('green'), attr('bold'), attr('reset')))
            return client
        except Exception as e:
            print(str(e))

