
import sys
import os
from paramiko import SSHClient
from __get_auth__ import Authorize
from progress import TqdmWrap
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from configparser import ConfigParser
from stat import S_ISDIR
from colored import fg, bg, attr
import ntpath
from pathlib import Path

home = str(Path.home())

path_file=home + "/.cloudtransport/history.txt"
ntpath.basename("a/b/c")


class Upload:
    
    def start_upload():
        try:
            client = Authorize.auth()
            sftp_client=client.open_sftp()
            print()
            
            local_path = prompt('Enter the local file or folder full path:', history=FileHistory(path_file))
            remote_dir = prompt('Enter the remote server file or folder full path:', history=FileHistory(path_file))
            print ('%s%s Upload Started... %s' % (fg('orchid'), attr('bold'), attr('reset')))
            with TqdmWrap(ascii=True, unit='b', unit_scale=True) as pbar:
                p=sftp_client.put(f'{local_path}',f'{remote_dir}',callback=pbar.viewBar)
            print ('%s%s upload Finished...%s' % (fg('orchid'), attr('bold'), attr('reset')))
                
            
            sftp_client.close()
            
            client.close()
        except  Exception as e:
            print(str(e))
            


   