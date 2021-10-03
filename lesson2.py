# A.

x = 5
y = 2, 7, 8

for i in y:
    if x > i:
        print('BIG')
    elif x < i:
        print('small')

# B.
[print(i) for i in range(5)]

# C.
numeric_seasons = 1, 2, 3, 4
for i in numeric_seasons:
    if i == 1:
        print('Summer')
    elif i == 2:
        print('Winter')
    elif i == 3:
        print('Fall')
    elif i == 4:
        print('Spring')

# D. Number 10 will be printed
count = 1
while count < 11:
    print(count)
    count = count + 1

# E.
age = 40
name = 'M'
currency_dollar_shekel = 3.24
flew_status = 'false'
appartment_number = 24

print(age, name, currency_dollar_shekel, flew_status, appartment_number)

# F.
phone_number = input('Please input your phone number')
print(phone_number)


# G.
def printhello():
    return str('Hello')


def calculate():
    return 5 + 3.2


printhello()
calculate()


# H.

def name_func(your_name):
    return your_name


def number_func(num):
    return num / 2


# I.

def sum_numbers(num1: int, num2: int):
    return num1 + num2


def add_strings(string1: str, string2: str):
    return " ".join([string1, string2])


# K.

for i in range(0, 5):
    print(("#" * i) + "#")

# M.

inputed_num = int(input("Input Number: "))


def sum_numbers(num: int):
    suma = num // 10 + num % 10
    return suma


sum_numbers(inputed_num)
