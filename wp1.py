#!/usr/bin/env python3

import webbrowser

"""
    Creating and viewing an HTML
    file using Python for Windows.
    Opens default browser window. 

"""


"""
    variable that opens new instance of html,
    assigns a file name, and 'w' designates
    that that this is a "write" program
"""

f = open('web_page_1.html','w')


# variable that stores html markup language
message = """<html>
<body>
<head>Stay tuned for our amazing summer sale!</head>
</body>
</html>"""


f.write(message) # writes the code to the newly created .html
f.close()  # closes the created file

# launches new browser tab in defaulf browser 
webbrowser.open_new_tab('web_page_1.html')



