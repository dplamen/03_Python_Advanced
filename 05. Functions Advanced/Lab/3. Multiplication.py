def multiply(*args):
    product = 1
    for num in args:
        product *= num
    return product


print(multiply(4, 5, 6, 1, 3))
