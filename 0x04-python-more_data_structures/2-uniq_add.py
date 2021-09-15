#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    new_list = []
    for element in my_list:
        if element not in new_list:
            add += element
            new_list.append(element)
    return add    
