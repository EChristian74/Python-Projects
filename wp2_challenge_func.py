#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.9.6
#
# Tk Ver:       8.6.9
#
# DB Browser for SQLite Version 3.12.2
#
# Author:       Eric Christian Boland
#
#
# Purpose:      Web Page Generator Program.  Incorporates OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationship.
#
#
# Tested OS:    This code was written and tested to work with Windows 10.


# Non-user defined import modules
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser


# Program code parsed and collated amongst three .py modules to keep code
# neat and orderly / the following modules must be imported to be accessed
import wp2_challenge_main
import wp2_challenge_gui


def center_window(self, w, h): # Passes in the tkinter frame (master) reference, plus w and h
    # Gets the user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # Calculates x and y coordinates to paint app centered on user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGo

# Catches if the user clicks on the windows upper-right 'X' to confirm they want to close
def ask_exit(self):
    if messagebox.askokcancel("Exit Program", "Are you sure you want to exit?"):
        # This closes the app
        self.master.destroy()
        os._exit(0)

# ========================================================================================================

"""
    variable that opens new instance of html,
    assigns a file name, and 'w' designates
    that that this is a "write" program
"""

# variable that will be called to open browser window
f = open('index.html','w')


# function to "get" entry data
def submit(self):
    # variable used to store entry data
    txtvar = self.txt_entry.get()

    # message variable that will be called to print user input to webbrowser
    
    message = """<html>
    <body>"""+txtvar+"""</body>
    </html>"""

         
    f.write(message) # writes the code to the newly created .html
    f.close()  # closes the created file
    # launches new browser tab in defaulf browser

    # call to open browser window
    webbrowser.open_new_tab('index.html')


"""
    Command "pass" ensures that all functions in gui.py
    file are controlled from main.py file
"""

if __name__ == "__main__":
    pass
                                                                 
                                                                                   
                                                                                   
                                                                                   


                                                                                
                            
