#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for element in range(x):
        try:
            print("{}".format(my_list[element]), end="")
            count++
        except: IndexError
            break
    print("")
    return count
