def math_operations(*args, **kwargs):
    for i in range(len(args)):
        try:
            if i % 4 == 0:
                kwargs['a'] += args[i]
            elif i % 4 == 1:
                kwargs['s'] -= args[i]
            elif i % 4 == 2:
                kwargs['d'] /= args[i]
            elif i % 4 == 3:
                kwargs['m'] *= args[i]
        except ZeroDivisionError:
            continue
    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(6, a=0, s=0, d=0, m=0))