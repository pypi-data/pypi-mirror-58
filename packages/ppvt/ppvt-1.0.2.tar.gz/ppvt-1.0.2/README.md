# Python Package Version Tool(ppvt)

Python-package-version-tool is a python package, which will helps to find the all, latest verion of gievn python package.

The main purpose of this package is to help the developers to check the latest version of python packages and their supported python version.


## Installation

> Prerequisites: Python:3.6
```bash
# Create seperate directory. 
$ sudo mkdir `your dir`
# Move to that directory.
$ cd your dir
# Install pip3
$ sudo apt-get install python3-pip
# Install Virtualenv
$ sudo pip3 install virtualenv
# Create virtual env
$ python3 -m venv env_name
# Activate Virtual env.
$ source /env_name/bin/activate
# Clone the repo.
$ git clone https://github.com/chatrapathik/python-package-version-tool.git
$ cd pypi-package-info
$ pip install -r requirements.txt
```

## Start Usage
```python
>> cd /pypi
>> Run the help command to get all the options.
$ python run.py -h
    usage: run.py [-h] [-r [INPUT_FILE]] [-p [PACKAGE]] [-o [OUTPUT_FILE]]
              [-l [LATEST]] [-a [ALL]] [-g [GREATER]]

    optional arguments:
      -h, --help 
          show this help message and exit
      -r [INPUT_FILE], --requirements [INPUT_FILE]
          Pass the requirements.txt file
      -p [PACKAGE], --package [PACKAGE]
          Pass the package name
      -o [OUTPUT_FILE], --output [OUTPUT_FILE]
          Pass the output file name
      -l [LATEST], --latest [LATEST]
          Filter only the latest version. By default it is True.
      -a [ALL], --all [ALL]
          To get all version of the package. By default it is False.
      -g [GREATER], --greater [GREATER]
          To get all versions greaterthan the given package version. By default it is False.

>> Check the latest version of given package.
$ python run.py -p django
Package Name : django, Package Version : 3.0.1, Required Python Version : >=3.4

>> Check all versions of given package.
$ python run.py -p django -a True
Package Name : django, Package Version : 2.1b1, Required Python Version : >=3.5
Package Name : django, Package Version : 1.11a1, Required Python Version : None
Package Name : django, Package Version : 2.0.13, Required Python Version : >=3.4
Package Name : django, Package Version : 2.0.12, Required Python Version : >=3.4

>> Check all the versions which are greater than specified package version.
$ python run.py -p django==3.0 -g True
Package Name : django, Package Version : 3.0.1, Required Python Version : >=3.4
>> Write output to csv file.
python run.py -p django==3.0 -g True -o versions.csv
```
