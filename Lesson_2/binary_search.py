#!/usr/bin/python3
# coding: utf-8

def binary_search (list, item): 
    low = 0                   # 0
    high = len (list) - 1     # 4-1 =3

    while low <= high:        # 0 <= 3
        mid = (low + high)    # mid = 3
        guess = list [mid]    # guess = list[3]
        if guess == item:     # 13 == 11
            return mid
        if guess > item:      # 13 > 11 
            high = mid -1     # 3 = 3 -1 => 2 = 11
        else: 
            low = mid + 1
    return None


my_list = [5, 9, 11, 13, 15]

print(binary_search(my_list, 15))