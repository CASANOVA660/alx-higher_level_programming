#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1 / my_list_2
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            res.append(div)
    return res
