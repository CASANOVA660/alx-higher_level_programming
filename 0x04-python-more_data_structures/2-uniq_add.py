#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = list(set(my_list))
    summ = 0
    for i in range(len(unique_list)):
        summ += unique_list[i]
    return summ
