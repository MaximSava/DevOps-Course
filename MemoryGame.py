import random
import os
from time import sleep

difficulty = int(input())


def generate_sequence(difficulty_number):
    """Will generate a list of random numbers between 1 to 101. The list
    length will be difficulty."""
    random_numbers_list = random.sample(range(1, 101), difficulty_number)
    print("We going to show random numbers.Are you ready to remember numbers?")
    for i in range(4, 0, -1):
        print(i, end='\r')
        sleep(1)
    print(random_numbers_list)
    sleep(0.7)
    print('\n' * 200)
    os.system('cls||clear')
    return random_numbers_list


def get_list_from_user(difficulty_number):
    """Will return a list of numbers prompted from the user. The list length
    will be in the size of difficulty."""
    user_list_numbers = [int(input()) for i in range(0,difficulty_number)]
    return user_list_numbers


def is_list_equal(generated_list, list_from_user):
    """- A function to compare two lists if they are equal. The function will return
    True / False."""
    if generated_list == list_from_user:
        return True
    else:
        return False


def play():
    gen_seq = generate_sequence(difficulty)
    list_from_user = get_list_from_user(difficulty)
    is_list_equal(gen_seq, list_from_user)
