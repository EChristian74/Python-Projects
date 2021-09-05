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
# Purpose:      Basic directory file transfer program. Program transfers
#               all files in source folder to destination folder.
#
#
# Tested OS:    This code was written and tested to work with Windows 10.


# Import the following modules
import os
import shutil


# Set where the source of the files are in folderA
source = 'C:/Users/timek/Desktop/FROM/'
print(source)

# Set the destination path to folderB
destination = 'C:/Users/timek/Desktop/TO/'
files = os.listdir(source)
print(destination)

for i in files:
    # Command to move the files represented by 'i' to the new destination
    shutil.move(source+i, destination)

    
