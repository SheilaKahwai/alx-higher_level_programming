#!/usr/bin/python3
def remove_char_at(str, n):
    for char in range(len(str.copy())):
        del str[n]
