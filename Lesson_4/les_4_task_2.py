#!/usr/bin/python3
# coding: utf-8

# Проанализировать скорость и сложность одного любого алгоритма из разработанных 
# в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, 
# для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

# В массиве случайных целых чисел поменять 
# местами минимальный и максимальный элементы

import timeit
import cProfile
import random
from random import random

## ВАРИАНТ №1

N = 5
arr = [0]*N
print('Изначальный массив: ')
for i in range(N):
    arr[i] = int(random()*5)
    print( arr[i], end = ' ')
print()

# mn = 0
# mx = 0
# for i in range(N):
#     if arr[i] < arr[mn]:
#         mn = i
#     elif arr[i] > arr[mx]:
#         mx = i
# b = arr[mn]
# arr[mn] = arr[mx]
# arr[mx] = b

# ## ВАРИАНТ №2
mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print('arr[%d]=%d arr[%d]=%d' % (imn+1, mn, imx+1, mx))
arr[imn],arr[imx] = arr[imx],arr[imn]

print('Поменяли местали max и min элементы: ') 
for i in range(N):
    print(arr[i], end=' ')
print()

## ВАРИАНТ №3
# count = int(input('Введите размер массива: '))
# a = [0] * count
# for i in range(count):
#     a[i] = int(random() * 100)
# print(a)

# min = 0
# max = 0
# for i in range(count):
#     if a[i] < a[min]:
#         min = i
#     elif a[i] > a[max]:
#         max = i
# b = a[min]
# a[min] = a[max]
# a[max] = b
# print(a)

# Тест с помощью timeit 
# Тест на размере массиа = 4 
#  - ВАРИАНТ №1
#  - ВАРИАНТ №2
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №3

# Тест на размере массиа = 14 
#  - ВАРИАНТ №1
#  - ВАРИАНТ №2
# 100 loops, best of 3: 0.0286 usec per loop - ВАРИАНТ №3

# Тест на размере массиа = 114
#  - ВАРИАНТ №1
#  - ВАРИАНТ №2
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №3