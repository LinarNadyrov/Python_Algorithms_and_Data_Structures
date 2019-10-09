#!/usr/bin/python3
# coding: utf-8

# В массиве найти максимальный отрицательный элемент. 
# Вывести на экран его значение и позицию в массиве.

from random import random
N = 5
arr = []
for i in range(N):
        arr.append(int(random() * 20) - 10)
print(arr)
 
i = 0
index = -1
while i < N:
        if arr[i] < 0 and index == -1:
                index = i
        elif arr[i] < 0 and arr[i] < arr[index]:
                index = i
        i += 1
 
print(' Максимальный отрицательный элемент: ', arr[index], '\n','Позиция: ', index+1 )