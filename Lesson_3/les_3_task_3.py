#!/usr/bin/python3
# coding: utf-8

# В массиве случайных целых чисел поменять 
# местами минимальный и максимальный элементы

# Первый вариант 
from random import random
N = 5
arr = [0]*N
print('Изначальный массив: ')
for i in range(N):
    arr[i] = int(random()*5)
    print( arr[i],end=' ')
print()
 
# 1-й вариант
mn = 0
mx = 0
for i in range(N):
    if arr[i] < arr[mn]:
        mn = i
    elif arr[i] > arr[mx]:
        mx = i
b = arr[mn]
arr[mn] = arr[mx]
arr[mx] = b

# 2-й вариант
# mn = min(arr)
# mx = max(arr)
# imn = arr.index(mn)
# imx = arr.index(mx)
# print('arr[%d]=%d arr[%d]=%d' % (imn+1, mn, imx+1, mx))
# arr[imn],arr[imx] = arr[imx],arr[imn]

print('Поменяли местали max и min элементы: ') 
for i in range(N):
    print(arr[i],end=' ')
print()