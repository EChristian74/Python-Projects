

# Creates protected class object

class Protected:
    def __init__(self):  # method that initializes attributes of the class
        self.__atm_pinVar = 7523  # defines variable, sets the initial value

    def getPrivate(self): # defines method to gather original value
        print(self.__atm_pinVar) # prints original value to display
        
    def setPrivate(self, private): # defines method to set new value
        self.__atm_pinVar = private # print new value to display

"""
    Obj "gets" or collects original private pin number,
    then "sets" or assigns new private pin number
"""

obj = Protected() 
obj.getPrivate()
obj.setPrivate(4536)
obj.getPrivate()




