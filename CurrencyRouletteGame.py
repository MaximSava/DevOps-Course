import requests
from GuessGame import generate_number, get_guess_from_user, compare_results

api_key = 'c13ba0d0f6b91ad89f19'

difficulty = int(input("Enter Difficulty Number:"))


def generate_number():
    """Generate an interval from amount a money and difficulty level"""
    total_value_money = int(input('Input amount of money to convert:'))
    url = "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=" + api_key
    response = requests.get(url)
    data = response.json()
    currency_rate = int(data['USD_ILS'])
    start_interval = (total_value_money * currency_rate) - (5 - difficulty)
    end_interval = (total_value_money * currency_rate) + (5 - difficulty)
    interval_list = list(range(start_interval, end_interval, 1))
    return interval_list


def get_guess_from_user():
    """ Will prompt the user for a number between 1 to difficulty and return the number."""
    user_input_num = int(input("Guess a value for amount of USD:"))
    return user_input_num


def play():
    interval_list = generate_number()
    guess_from_user = get_guess_from_user()
    result = compare_results(interval_list, guess_from_user)
    print(result)


interval_list2 = list(range(1, 10, 1))
if 11 in interval_list2:
    print(True)
else:
    print(False)
