

import sqlite3


# file list from which script will write to db


conn = sqlite3.connect('files.db')

with conn:  # do this while we are using db
    cur = conn.cursor()  # invokes cursor object, then below sql statement passed in to open db
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file_names ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file_name STRING \
        )")  # sql string statement
    conn.commit()  # commits the change
conn.close() # closes the connection to db



conn = sqlite3.connect('files.db')  # re-connects to db

# list from which for loop will gather data and write to db
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loops through each object in list above to gather file names that end in 'txt'
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            # the value for each row in db will be one file name out of the tuple
            # and will denote one element tuple for each file name per row ending with 'txt'
            cur.execute("INSERT INTO tbl_file_names(col_file_name) VALUES (?)", (x,))
            print(x) # final command to print to console data written to db


