#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        print("{}".format((number * (-1)) % 10), end='')
        number = ((number * (-1)) % 10)
        return number
    else:
        print("{}".format((number % 10), end=''))
        return (number % 10)

