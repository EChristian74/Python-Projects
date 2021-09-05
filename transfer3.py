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
# Purpose:      Directory file transfer program with control GUI. Program allows
#               user to select source and destination using a GUI, to view the
#               source and destination in entry widget fields, then to execute
#               a 'check' file audit and move the files.
#
#
# Tested OS:    This code was written and tested to work with Windows 10.


# Import the following modules
import os
import time
import shutil
import datetime
import glob
from tkinter import *
import tkinter.filedialog as filedialog
import tkinter as tk
from tkinter import messagebox
import pyautogui


# Variable to find the difference
# between two datetime objects
SECONDS_IN_DAY = 24 * 60 * 60


# Variables to designate source
# and destination directory folders
def src():
    input_path = tk.filedialog.askdirectory()
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'


def dst():
    output_path = tk.filedialog.askdirectory()
    output_entry.delete(1, tk.END)  # Remove current text in entry
    output_entry.insert(0, output_path)  # Insert the 'path'


# Variables to establish the current time
# for comparison against file modification
# date and time
now = datetime.datetime.now()
before = now - datetime.timedelta(hours=24)


# Function to call the last time
# files in directory were modified
def last_mod_time():
    sourcepath = input_entry.get()
    destpath = output_entry.get()
    print(sourcepath)
    print(destpath)
    for fname in os.listdir(sourcepath):
        src_fname = os.path.join(sourcepath, fname)
        print(src_fname)
        mtime = os.path.getmtime(src_fname)
        modtime = datetime.datetime.fromtimestamp(mtime)
        print(modtime)
        print(before)
        if modtime > before:
            shutil.move(src_fname, destpath)


master = tk.Tk()

# Defines the master frame configuration
top_frame = tk.Frame()
master.title("Tech Academy File Manager v1.0")
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

top_frame.pack(side=TOP)
line.pack(pady=10)
bottom_frame.pack(side=BOTTOM)
      

# Defines source widget label and data entry field
input_path = tk.Label(top_frame, text="Source File Path:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=src)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)


# Defines destination widget label and data entry field
output_path = tk.Label(bottom_frame, text="Destination File Path:")
output_entry = tk.Entry(bottom_frame, text="", width=40)
browse2 = tk.Button(bottom_frame, text="Browse", command=dst)

output_path.pack(pady=5)
output_entry.pack(pady=5)
browse2.pack(pady=5)


# Defines the button which executes the 'file check' and file transfer
begin_button = tk.Button(bottom_frame, text='Validate and Transfer Files!', command=last_mod_time)
begin_button.pack(pady=20, fill=tk.X)







