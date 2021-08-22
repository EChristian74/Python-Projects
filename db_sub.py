

import sqlite3

import glob, os


# method to connect to a database

"""
    the below creates variable using class sqlite3 to 
    connect to database using method of connect() 
    also creates our empty database
"""
conn = sqlite3.connect('files.db')

with conn:  # do this while we are using database
    cur = conn.cursor()  # invokes the cursor object, then below is sql string statement passed in and database is opened
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file_names ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name STRING \
        )")  # sql string statment
    conn.commit()  # commits the change
conn.close() # closes the connection to database



conn = sqlite3.connect('files.db')  # re-connects to database
                                 
with conn:  # do this while we are using database
    cur = conn.cursor()  # invokes the cursor object, then below is sql string statement passed in and database is opened
    cur.execute("INSERT INTO tbl_file_names(col_name) VALUES(?)", \
                ('information.docx',))  # string value sql statement
    cur.execute("INSERT INTO tbl_file_names(col_name) VALUES(?)", \
                ('Hello.txt',))  # string value sql statement
    cur.execute("INSERT INTO tbl_file_names(col_name) VALUES(?)", \
                ('myImage.png',))  # string value sql statement
    cur.execute("INSERT INTO tbl_file_names(col_name) VALUES(?)", \
                ('myMovie.mpg',))  # string value sql statement
    cur.execute("INSERT INTO tbl_file_names(col_name) VALUES(?)", \
                ('World.txt',))  # string value sql statement
    cur.execute("INSERT INTO tbl_file_names(col_name) VALUES(?)", \
                ('data.pdf',))  # string value sql statement
    cur.execute("INSERT INTO tbl_file_names(col_name) VALUES(?)", \
                ('myPhoto.jpg',))  # string value sql statement
    conn.commit()  # commits the change
conn.close()  # closes the connection to the database
                


conn = sqlite3.connect('files.db') # re-connects to database


with conn:  # do this while we are using database
    cur = conn.cursor()  # invokes the cursor object, then below is sql string statement passed in and database is opened
    cur.execute("SELECT col_name FROM tbl_file_names WHERE col_name LIKE '%txt'") # tuple - fixed data
    varName = cur.fetchall()  # stores data as variable, so isn't lost
    for item in varName:
        msg = "File Name: {}".format(item[0])  # calling data using wildcard
    print(msg)  

                                 
