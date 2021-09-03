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
import wp2_challenge_main
import wp2_challenge_func

# Loads gui widgets when called by main
def load_gui(self):
    """
        Defines default tkinter widgets and their initial
        configuration and placed them using grid geometry
    """
    
    self.lbl_entry = tk.Label(self.master,text='Enter Data Here')
    self.lbl_entry.grid(row=0,column=0,padx=(34,0),pady=(12,0),sticky=N+W)
    
    self.txt_entry = tk.Entry(self.master,text='')
    self.txt_entry.grid(row=2,column=0,rowspan=1,columnspan=2,padx=(20,0),pady=(20,0),sticky=N+E+W)
   
    self.btn_submit = tk.Button(self.master,width=14,height=2,text='Submit Data',command=lambda: wp2_challenge_func.submit(self))
    self.btn_submit.grid(row=6,column=0,padx=(20,0),pady=(17,0),sticky=N+S+E+W)


"""
    Command "pass" ensures that all functions in gui.py
    file are controlled from main.py file
"""


if __name__ == "__main__":
    pass
