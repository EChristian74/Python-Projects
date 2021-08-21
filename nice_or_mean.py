#
# Python 3.9.6 
#
# Author: Eric C. Boland
#
# Purpose: The Tech Academy - Python Courswe, creating our first program together.
#          Demonstrating how to pass variables from function to function
#          while producing a functional game.  
#
#          Remember, function_name(variable) means that we pass in the variable.
#          return variable means that we are returning the variable to  
#          back to the calling function.

# import winsound module for opening of game

import winsound
# play sound at open
winsound.PlaySound("GameOpen", winsound.SND_ALIAS)


# open greeting

open =   "Nice, MEAN, namE...PLAY NOW!"   
print(open)


# starting function

def start(nice=0,mean=0,name=""): # default parameters and values, will acquire during game and store in these variables, then defaults will be overwritten
    # get user's name
    name = describe_game(name)  # creating variable, call function describe_game, pass in (name) that is empty at the start
    nice,mean,name = nice_mean(nice,mean,name)  # nice,mean,name (variables) | nice_mean(nice,mean,name) (function passing in variables), then will return and store values


def describe_game(name):  # function describe_game | parameter (name)
    """  
        Check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game.
    """
    # meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name
    if name != "":  # decision-making logic, variable "name" if value not equal(!=), if not empty do next line
        print("\nThank you for playing again, {}!".format(name))  # will be used if player plays more than once
    else:  # will fire in the beginning because since name will be empty at first
        stop = True  # only true if name is empty 
        while stop == True:  # means "while stop is True", then do following loop
            if name == "":  # if name is empty, do next steps
                name = input("\nWhat is your name? \n>>> ").capitalize()  # once name input, capitalize (built-in method for strings)
                if name != "":  # if name not empty, do greeting msg       # remember, data from user is a "raw string"
                    print("\nWelcome, {}!".format(name))  # .format is built-in function using "wildcards"
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")  # \n = escape sequence for new line
                    stop = False  # now that we have user's name, no longer need to ask for name
                                  # False stops block of code starting from True
    return name  # now that we have stored the user's name, it will be stored in "describe_game(name)" 
            

def nice_mean(nice,mean,name):  # function calls in user's name from (nice,mean,name) at the top, nice and mean are still default of "0"
    stop = True  # only true if 
    while stop:
        show_score(nice,mean,name)  # new function, pass in (nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()  # 3 chevrons for looks + user queue
        if pick == "n":  # if user picks "n", then do next line + change the value of nice
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)  # if nice + 1, stop loop 
            stop = False
        if pick == "m":  # if user picks "m", then do next line + change value of mean 
            print("\nThe stranger glares at  you \nmenacingly and storms off...")
            mean = (mean + 1)  # if mean = 1, stop loop
            stop = False
    score(nice,mean,name)  # function to pass the 3 variables to the score()
        
                     
def show_score(nice,mean,name):  # passing in (nice,mean,name) score so far and name from previous block
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))




def score(nice,mean,name):
    # score function being passed the values stored within the 3 variables
    if nice > 2:  # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2:  # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:         #else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)  # neither nice or mean conditions met, go back to "def nice_mean(nice,mean,name)"
                                   # user's name and score so far would still be stored for the next round
                                   # until nice or mean > 2


def win(nice,mean,name):  # calls (nice,mean,name) score and user's name
    # substitute the {} wildcards with our variables values
    print("\nNice job {}, you win! \nEveryone love you and you've \nmade lots of friends along the way!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)  # asking if user wants to play again


def lose(nice,mean,name):  # calls (nice,mean,name) score and user's name
    # substitute the {} wildcards with our variables values
    print("\nAhhh to bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)  # even though lost, going to call function to ask if want to play again


def again(nice,mean,name):  # pass in (nice,mean,name) scores and user's name
    stop = True
    while stop:  # while stop True go to next step
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":  # if user response "y", stop ask loop, reset game
            stop = False
            reset(nice,mean,name)
        if choice == "n":  # if user response "n", stop ask loop, quit game
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()  # prompt to close Python in development mode
        else: print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")  # if neither yes or no, restates 
                                                                       # the question + asks for response
                                                                       # then would start the again loop again

def reset(nice,mean,name):  # pass in (nice,mean,name) scores and user's name
    nice = 0  # resets nice back to default of "0"
    mean = 0  # resets nice back to default of "0"
    # notice, I do not reset the name variable as the same user has elected to play again, name still stored
    start(nice,mean,name) # calls "def start(nice=0,mean=0,name="")" at the very beginning,
                          # except this time, name is not ""

if __name__ == "__main__":
    start()
