#!/usr bin python

"""
    #!/usr/bin/python
    It's a recommended way, proposed in documentation:
    2.2.2. Executable Python Scripts.
    In a Unix-like operating system, the program loader
    takes the presence of these two characters as an
    indication that the file is a script, and tries to
    execute that script using the interpreter specified
    by the rest of the first line in the file.
"""

# -*- coding: utf-8 -*-
"""
    # -*- coding: utf-8 -*-
    This sets the charset if it is present on the first two lines of the file.
    This is Syntax to declare the encoding of a Python source file. It's discusssed
    in the PEP 0263 - Defining Python Source Code Encodings.
    https://www.python.org/dev/peps/pep-0263/
"""

#
# Python Ver:   3.9.6
#
#
# Author:       Eric Christian Boland
#
#
# Purpose:      Basic directory file transfer program.  Program transfers
#               only those files modified in the past 24 hours from
#               source folder to destination folder. 
#
#
# Tested OS:    This code was written and tested to work with Windows 10.


# Import the following modules
import os
import time
import shutil
import datetime
from tkinter import *
import tkinter.filedialog as filedialog
import tkinter as tk


# Variable to find the difference
# between two datetime objects
SECONDS_IN_DAY = 24 * 60 * 60


src = 'C:/Users/timek/Desktop/FROM/'
print(src)

dst = 'C:/Users/timek/Desktop/TO/'
print(dst)

# Variables to designate source
# and destination directory folders

# Variables to establish the current time
# for comparison against file modification
# date and time
now = datetime.datetime.now()
before = now - datetime.timedelta(hours=24)


# Function to call the last time
# files in directory were modified
for fname in os.listdir(src):
    src_fname = os.path.join(src, fname)
    print(src_fname)
    mtime = os.path.getmtime(src_fname)
    modtime = datetime.datetime.fromtimestamp(mtime)
    print(modtime)
    print(before)
    if modtime > before:
        shutil.move(src_fname, dst)




            
