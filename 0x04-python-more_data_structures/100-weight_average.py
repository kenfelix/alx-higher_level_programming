#!/usr/bin/python3
def weight_average(my_list=[]):
    add = 0
    base = 0
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    for element in my_list:
        add += (element[0] * element[1])
        base += element[1]
    return (add / base)
