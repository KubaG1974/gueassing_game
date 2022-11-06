import math
import random
TIMES_TO_PLAY = 10

a = [] #declare empty list as variable a

for i in range (TIMES_TO_PLAY):
    a.append(random.randint(1, 99)) #append list with random int between 1 and 99

def ask_for_input(maxvalue):
    user_number = int(input(f"Enter an integer from 1 to {maxvalue}: "))
    return user_number

for i in range(10): #create loop that will repeat itself for i between 0 and 9
    g= None
    while a[i] != g: #loop checks every element of list a  against the value of user input g
        g = ask_for_input(99)
        if g < a[i]: #checks if input less than consecutive elements of list a
            print("guess is low") #display message in console
        elif g > a[i]: #otherwise if input more than consecutive elements of list a
            print("guess is high") #display message in console
    print("you guessed it!") #display message in console

b = []
for i in range (TIMES_TO_PLAY):
    b.append(random.randint(1, 49))
for i in range(10):
    g = None
    while a[i] != g: #loop checks every element of list a  against the value of user input g
        g = ask_for_input(49)
        if g < a[i]: #checks if input less than consecutive elements of list a
            print("guess is low") #display message in console
        elif g > a[i]: #otherwise if input more than consecutive elements of list a
            print("guess is high") #display message in console
    print("you guessed it!")