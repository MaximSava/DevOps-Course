import random


def generate_number():
    # generate random number and save it to var secret_number
    difficulty = int(input('Input difficulty number:'))
    secret_number = random.randrange(1, difficulty)
    return secret_number


def get_guess_from_user():
    """ Will prompt the user for a number between 1 to difficulty and return the number."""
    user_input_num = int(input("Guess generated difficulty number:"))
    return user_input_num


def compare_results(secret_number, user_guessed_number):
    """ Will compare the the secret generated number to the one prompted by the get_guess_from_user."""
    if user_guessed_number == secret_number:
        return True
    else:
        return False


def play():
    """ Will call the functions above and play the game. Will return True / False if the user lost or won."""
    sec_number = generate_number()
    guessed_num = get_guess_from_user()
    compare_num = compare_results(sec_number, guessed_num)
    return print(compare_num)
