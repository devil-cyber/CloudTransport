import os
import shutil
import sys
from sys import platform
from pathlib import Path
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

home = str(Path.home())
directory = '.cloudtransport'
path = os.path.join(home,directory)

try:
	os.mkdir(path)
	with open(path +'/config.ini','w+') as fp:
		pass
	with open(path +'/history.txt','w+') as fp:
		pass
except OSError as e:
	print(f'The folder {directory} already exist inside {home}')
	print()
	while True:
		delete = input(f'Do you want to remove folder {directory} yes or no: ')
		if delete=='yes' or delete=='y':
			shutil.rmtree(path)
			print('Folder Deleted Successfully!!!')
			break
		elif delete=='no' or delete=='n':
			break
		else:
			print()
			print('Give input yes or y | no or n only')
			print()




setup(
    name = 'CloudTransport',
    version = '0.0.1',
    author = 'Manikant Kumar',
    author_email = 'mani2474695@gmail.com',
    license = 'MIT',
    description = 'A light weight CLI tool to upload and download file from remote server',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://gtihub.com/devil-cyber/CloudTransport',
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
)
if platform=='linux':
	print()
	print('************************************************')
	print('Add this script to .bashrc')
	print(f"alias cloud='python3 -W ignore {os.getcwd()}/terminal.py'")
	print(f"source ~/.bashrc")