# a)

from operator import __add__, __mul__, __truediv__

first, second = 7, 44.3
[print(i(second, first)) for i in [__add__, __mul__, __truediv__]]

# b)
a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8

print(a, b, c)

# c)
#   1.  Where is no differences but
#   generally, double quotes are used for string representation and single quotes are used for regular expressions

#   2.
my_number = int(5 + 5)
print("result is: " + str(my_number))

#   d)
x = 5
y = 2.36
print(x + int(y))

# Answer 7


#   Challenge

a = 8
b = "123"
print(a + int(b))
