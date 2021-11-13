import functools as ft
def operate(operator, *args):
    return ft.reduce(lambda x, y: eval(str(x) + operator + str(y)), args)


print(operate("*", 3, 4))