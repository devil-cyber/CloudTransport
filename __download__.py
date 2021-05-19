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

config_path = home + "/.cloudtransport/config.ini"
path_history = home + "/.cloudtransport/history.txt"
ntpath.basename("a/b/c")



class Download:
    
    def start_download():
        try:
            
            client = Authorize.auth()
            sftp_client=client.open_sftp()
            
            def isdir(path):
                try:
                    return S_ISDIR(sftp_client.stat(path).st_mode)
                except IOError:
                    return False
            def path_leaf(path):
                head, tail = ntpath.split(path)
                return tail,head
            config_object = ConfigParser()

            config_object.read(config_path)
            server_info = config_object['SERVERINFO']
            username = server_info['username']
            
            print()
            remote_dir = prompt('Enter the remote server file or folder path:', history=FileHistory(path_history))
            p_path,head=path_leaf(remote_dir)
           
            
            if isdir(remote_dir):
                # sftp_client.chdir(f'head')
                # (stdin, stdout, stderr) = client.exec_command('ls')
                # for line in stdout.readlines():
                #     print(line)
                client.exec_command(f'tar -cf {p_path}.tar {remote_dir}')
                print ('%s%s Download Started... %s' % (fg('orchid'), attr('bold'), attr('reset')))
                with TqdmWrap(ascii=True, unit='b', unit_scale=True) as pbar:
                    sftp_client.get(f'/home/{username}/{p_path}.tar',f'{p_path}.tar',callback=pbar.viewBar)
                print ('%s%s Download Finished...%s' % (fg('orchid'), attr('bold'), attr('reset')))
                
            else:
                print ('%s%s Download Started... %s' % (fg('orchid'), attr('bold'), attr('reset')))
                with TqdmWrap(ascii=True, unit='b', unit_scale=True) as pbar:
                    sftp_client.get(f'{remote_dir}',f'{p_path}',callback=pbar.viewBar)
                print ('%s%s Download Finished...%s' % (fg('orchid'), attr('bold'), attr('reset')))
            
            sftp_client.close()
            
            client.close()
        except  Exception as e:
            print('Error from download section:',str(e))
            


   