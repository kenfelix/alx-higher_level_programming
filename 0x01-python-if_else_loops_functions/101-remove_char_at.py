#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(0, n):
        print("{}".format(str[i]), end='')
    for j in range(n + 1, len(str)):
        print("{}".format(str[j]), end='')

