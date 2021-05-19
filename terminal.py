#!/usr/bin/env python3
# GNU All-Permissive License
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.

import argparse
import sys
import os
from config import Config
from __download__ import Download
from colored import fg, bg, attr
from invalid_flag import __set__flag__, __down__flag__,__up__flag__
from configparser import ConfigParser
from __download__ import Download
from __upload__ import Upload
from art import *
from pathlib import Path
home = str(Path.home())

config_path = home + '/.cloudtransport/config.ini'

config_object = ConfigParser()

def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Useful command")
    parser.add_argument("-s", "--set", help="To set configuration for the remote server")
    parser.add_argument("-d", "--download", help="To download a file from remote server")
    parser.add_argument("-u", "--upload", help="To upload a file to remote server")
    parser.add_argument("-c", "--cmd", help="To run command on remote server")
    options = parser.parse_args(args)
    return options


if __name__ == "__main__":
    options = getOptions(sys.argv[1:])
    df = options.download
    df1 = options.upload
    df2 = options.set
    none_len = len(str(df)+str(df1)+str(df2))
    if df2 !=None or none_len==12:
        print("**********************************************************************")
        tprint("CloudTransport")
        print (f'%s%sA python script to Download and Upload file on remote server%s' % (fg('green_3b'), attr('bold'), attr('reset')))
        print (f'%s%sDeveloped By Manikant Kumar%s' % (fg('green_3b'), attr('bold'), attr('reset')))
        print("**********************************************************************")

    if options.set != None:
        if options.set == 'c' or options.set=='C':
            Config.set_config()
        else:
            print (f'%s%s {__set__flag__} %s' % (fg('green_3b'), attr('bold'), attr('reset')))
            sys.exit()
    if options.download != None:
        if df == 'r' or df == 'R':
            try:
                config_object.read(config_path)
                config_object["SERVERINFO"]
            except Exception as e:
                print('Error in config file:',str(e))
                print('Set Configuration again')

                Config.set_config()
                Download.start_download()
                sys.exit()
            Download.start_download()
        else:
            print (f'%s%s {__down__flag__} %s' % (fg('green_3b'), attr('bold'), attr('reset')))
            sys.exit()
    if options.upload != None:
        if df1 == 'r' or df1 == 'R':
            try:
                config_object.read(config_path)
                config_object["SERVERINFO"]
            except Exception as e:
                print('Error in config file:',str(e))
                print('Set Configuration again')
                Config.set_config()
                Upload.start_upload()
                sys.exit()
            Upload.start_upload()
        else:
            print (f'%s%s {__up__flag__} %s' % (fg('green_3b'), attr('bold'), attr('reset')))
            sys.exit()


