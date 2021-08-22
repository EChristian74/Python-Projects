


import os, sys  # built in module, no need to install

import os.path, time


fName = 'os_list_dir'  # new string

fPath = 'C:\\OS\\script_assignment\\_list_dir.txt'  # new string

abPath = os.path.join(fPath, fName)  # allows us to concatenate fPath and fName
print(abPath)


dirctx = os.listdir('C:\\OS\\script_assignment')   # creates variable for printing list of files in directory
print('\nDirectory and files:\n')  # creates variable for printing of files in directory to display
print(dirctx)  # calls variable to print (iterates) list of files in directory to display


# print methods below print the file name and last modified date, time, etc. for .txt files in directory
print('\nos_list_dir.txt,', 'Last modified: %s' % time.ctime(os.path.getmtime('C:\\OS\\script_assignment\\os_list_dir.txt')))

print('\nos_path_join.txt,', 'Last modified: %s' % time.ctime(os.path.getmtime('C:\\OS\\script_assignment\\os_path_join.txt')))
