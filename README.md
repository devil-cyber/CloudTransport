# CloudTransport
[![devil-cyber - CloudTransport](https://img.shields.io/static/v1?label=devil-cyber&message=CloudTransport&color=blue&logo=github)](https://github.com/devil-cyber/CloudTransport)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
`Transfer or Download file from remote server with ease of CLI`
## Overview
`CloudTransport a light weight python script that uses sftp transfer protocol to transfer files between the server 
with the ease of CLI`

## Problem and Goals
- Currently it has been tesetd over ubuntu machine only
- In future we will update its other os dependent script
- Contribution is welcome 

## How to install ?
`Follow these steps to install and if python does not work use python3l`
```sh
# Clone this project
git clone https://github.com/devil-cyber
# After cloning go to the project directory & run
python install setup.py
# At last add a alias to .bashrc 
cloud alias='python -W ignore {path to project directory}/terminal.py'

## Now you are good to go! you can run file from any directory now
```


## How to use
`Follow these steps:`
## About
- #### To know about the CLI tool type following command in terminal
```sh
cloud
```
> Output will look like
![About](https://github.com/devil-cyber/asset/raw/main/about.png)

## Set Configuration
- #### To used this tool first we have to set some configuration.
- #### Configuration is used by remote server to Authenticate the user.
- #### Configuration look like:-
    * **Give Hostname  ie. (Public Ip Adress of your remote server)**
    * **Give private key path ie.(Your cloud provider provides a private key file so give that file path)**
    * **Give port ie. (Your remote server port )**
    * **Give username ie. (This is username of your remote VM)**
> Just like this:-
![config](https://github.com/devil-cyber/asset/raw/main/set_config1.png)
![config](https://github.com/devil-cyber/asset/raw/main/newc.png)
#### To set configuration write following command in terminal
```sh
cloud --set c
```
> Output will look like:-
![config](https://github.com/devil-cyber/asset/raw/main/nec.png)

## Download
- #### After configuration setting we can download any file or folder from remote server.
- #### Provide some details:-
    * **Enter server file or folder path  ie. (Give the path of folder or file that you wants to download from remote srver)**
> Just like this:-
![download](https://github.com/devil-cyber/asset/raw/main/download1.png)
![download2](https://github.com/devil-cyber/asset/raw/main/download2.png)
#### To start download write following code in terminal
```sh
cloud --download r
```
> Output will look like:-
![download3](https://github.com/devil-cyber/asset/raw/main/download3.png)


## Upload
- #### After configuration setting we can upload any file or folder to remote server.
- #### Provide some details:-
`Note for uploading folder firts make a zip file then upload that` 
`Note At time of entering remote server folder path provide the the same extension of the file as in local syatem to save on server` 
eg. Local path : /home/path/exmaple.zip
    Remote path : /home/anypath/myfile.zip
    * **Enter local file or folder full path ie.(Enter the full path of the including your file path)**
    *  **Enter server file or folder full path ie. (Enter the path on which you wants to save uploaded file with same extension as in local computer**
> Just like this:-
![download](https://github.com/devil-cyber/asset/raw/main/upload1.png)
![download2](https://github.com/devil-cyber/asset/raw/main/upload3.png)
#### To start download write following code in terminal
```sh
cloud --download r
```
> Output will look like:-
![download3](https://github.com/devil-cyber/asset/raw/main/upload3.png)



## License

Released under [MIT](/LICENSE) by [@devil-cyber](https://github.com/devil-cyber).


