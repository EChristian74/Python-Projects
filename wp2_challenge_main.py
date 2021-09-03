#!/usr/bin/python
"""
    #!/usr/bin/python
    It's a recommended way, proposed in documentation:
    2.2.2. Executable Python Scripts.
"""
# -*- coding: utf-8 -*-
"""
    # -*- coding: utf-8 -*-
    Sets the charset and Syntax declares the encoding of Python source file.
    See: PEP 0263 - Defining Python Source Code Encodings.
    https://www.python.org/dev/peps/pep-0263/
"""
#
# Python Ver:   3.9.6
#
# Tk Ver:       8.6.9
#
# DB Browser for SQLite Version 3.12.2
#
# Author:       Eric Christian Boland
#
# Purpose:      Web Page Generator Program. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
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
import wp2_challenge_gui
import wp2_challenge_func
   

# Frame is the Tkinter frame class that user-defined class will inherit
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Defines master frame configuration
        self.master = master
        self.master.minsize(170,160) #(Width, Height)
        self.master.maxsize(170,160)
        # CenterWindow method centers app on the user's screen
        wp2_challenge_func.center_window(self,180,160)
        self.master.title("Web Page Generator")
        self.master.configure(bg="#F0EAEA")
        # tkinter protocol built-in method to catch if 
        # User clicks the upper corner, "X" on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: wp2_challenge_func.ask_exit(self))
        arg = self.master

        # Loads in the GUI widgets from module
        wp2_challenge_gui.load_gui(self)
        
        # Instantiates Tkinter menu dropdown object
        # Menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: wp2_challenge_func.ask_exit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar

        """
            Config method of the widget applied to display menu
        """

        self.master.config(menu=menubar, borderwidth='1')
   
"""
    Python begins gui and application in sequence of code below if __name__ == "__main__"

    root = tk.Tk()              # Instantiates the Tk.() root frame (window) into being
    App = ParentWindow(root)    # Instantiates user-defined class as an App object
    root.mainloop()             # Controls Tkinter class object, the window, to keep looping
                                # until we instruct it to close
"""

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
