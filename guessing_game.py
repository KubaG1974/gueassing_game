from random import randint
TIMES_TO_PLAY = 10


def generate_random_numbers_list(maxvalue):
    random_number_list = []
    for _ in range(TIMES_TO_PLAY):
        random_number_list.append(randint(1,maxvalue))
        
    return random_number_list
    

def ask_for_input(maxvalue):
    user_number = int(input(f"Enter an integer from 1 to {maxvalue}: "))
    return user_number

def AIplayer():
    pass

def game_logic(maxvalue, random_number_list):
    random_numbers_list = generate_random_numbers_list(maxvalue)
    for i in range(TIMES_TO_PLAY):
        user_input= None
        while random_number_list[i] != user_input:
            user_input = ask_for_input(maxvalue)
            if user_input < random_number_list[maxvalue]: 
                print("guess is low") 
            elif user_input > random_number_list[i]: #otherwise if input more than consecutive elements of list a
                print("guess is high") #display message in console
    print("you guessed it!") #display message in console


game_logic(99)
game_logic(49)