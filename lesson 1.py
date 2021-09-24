from operator import __add__, __mul__, __truediv__
first, second = 7, 44.3
[print(i(second,first)) for i in [__add__,__mul__,__truediv__]]
