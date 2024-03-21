#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    Printed = 0
    try:
        for i in range(x):
            if not isinstance(my_list[i], int):
                pass
            else:
                print("{:d}".format(my_list[i]), end="")
                Printed += 1
    except IndexError:
        print("")
    return Printed
