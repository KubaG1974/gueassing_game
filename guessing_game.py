import math
import random
TIMES_TO_PLAY = 10
def generate_random_numbers_list(maxvalue):
    random_number_list = []
    for i in range(TIMES_TO_PLAY):
        random_number_list.append(random.randint(1,maxvalue))
        
    return random_number_list
    

a = generate_random_numbers_list(99)

def ask_for_input(maxvalue):
    user_number = int(input(f"Enter an integer from 1 to {maxvalue}: "))
    return user_number

for i in range(TIMES_TO_PLAY): #create loop that will repeat itself for i between 0 and 9
    user_input= None
    while a[i] != user_input: #loop checks every element of list a  against the value of user input g
        g = ask_for_input(99)
        if user_input < a[i]: #checks if input less than consecutive elements of list a
            print("guess is low") #display message in console
        elif user_input > a[i]: #otherwise if input more than consecutive elements of list a
            print("guess is high") #display message in console
    print("you guessed it!") #display message in console

b = generate_random_numbers_list(49)
for i in range(TIMES_TO_PLAY):
    user_input = None
    while a[i] != user_input: #loop checks every element of list a  against the value of user input g
        user_input = ask_for_input(49)
        if user_input < a[i]: #checks if input less than consecutive elements of list a
            print("guess is low") #display message in console
        elif user_input > a[i]: #otherwise if input more than consecutive elements of list a
            print("guess is high") #display message in console
    print("you guessed it!")