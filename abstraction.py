


from abc import ABC, abstractmethod

# Python program showing abstract base class 

# parent class
class Event(ABC): # declares parent class 
    def cover(self, amount):
        print("Your cover charge is ",amount)
        # function that passes undefined argument
        @abstractmethod  
        def ticket(self, amount):
            pass

# child class 1
# defines how to implement function from parent class
class Floor(Event):
    def ticket(self, amount):
        print('Your floor seat ticket charge is {}.'.format(amount))

# child class 2
# defines how to implement function from parent class
class Box(Event):
    def ticket(self, amount):
        print('Your box seat ticket charge is {}.'.format(amount))

# Object calls both the parent class and child class 1 method
obj = Floor()
obj.cover("$40")
obj.ticket("$40")

# Object calls both the parent class and child class 2 method
obj = Box()
obj.cover("$40")
obj.ticket("$80")
