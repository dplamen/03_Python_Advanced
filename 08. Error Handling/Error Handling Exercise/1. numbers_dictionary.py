numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')
    line = input()

searched = input()
while searched != "Remove":
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print('Number does not exist in dictionary')
    searched = input()

searched = input()
while searched != "End":
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print('Number does not exist in dictionary')
    searched = input()

print(numbers_dictionary)
