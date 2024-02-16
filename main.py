import math
import random

def start_game():

    # possible difficulty levels
    posble_difficulty_lvl = ['easy', 'medium', 'hard']

    # user chosen difficulty level
    user_difficulty_lvl = input('Enter difficulty level (easy, medium, hard) : ')

    # range for different difficulty level
    if user_difficulty_lvl == 'easy':
        lower_num, upper_num = 1, 100
    elif user_difficulty_lvl == 'medium':
        lower_num, upper_num = 1, 1000
    else:
        lower_num, upper_num = 1, 10000

    # number of tries available according to difficulty level
    user_tries_avlbl = int(math.log2(upper_num)) + 1
    
    # number picked by computer randomly
    computer_num = random.randint(lower_num,upper_num)
    
    for i in range(user_tries_avlbl):
        
        user_num = int(input('Enter number : '))
        
        if user_num == computer_num:
            print(f'Congratulations ! Number found on {i+1} attempt.')
            break
        elif user_num > computer_num:
            print(f'Guess lower. Number of attempts available = {user_tries_avlbl - i - 1}')
        else:
            print(f'Guess higher. Number of attempts available = {user_tries_avlbl - i - 1}')

if __name__ == '__main__':
    start_game()
