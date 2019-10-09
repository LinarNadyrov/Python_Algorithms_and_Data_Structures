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

count = int(input('Введите размер массива: '))
array = [0] * count
for i in range(count):
    array[i] = int(random() * 100)
print(array)

## ВАРИАНТ №1
mn = 0
mx = 0
for i in range(count):
    if array[i] < array[mn]:
        mn = i
    elif array[i] > array[mx]:
        mx = i
b = array[mn]
array[mn] = array[mx]
array[mx] = b

print('Поменяли местали max и min элементы: ') 
for i in range(count):
    print(array[i], end = ' ')
print()

## ВАРИАНТ №2
mn = min(array)
mx = max(array)
imn = array.index(mn)
imx = array.index(mx)
array[imn],array[imx] = array[imx],array[imn]

print('Поменяли местали max и min элементы: ') 
for i in range(count):
    print(array[i], end = ' ')
print()

## ВАРИАНТ №3
array[array.index(max(array))], array[array.index(min(array))] = array[array.index(min(array))], array[array.index(max(array))]
print(array)

# Тест с помощью timeit 
# Массив из 3 элементов
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №1
# 100 loops, best of 3: 0.031 usec per loop - ВАРИАНТ №2
# 100 loops, best of 3: 0.0405 usec per loop - ВАРИАНТ №3

# Массив из 9 элементов
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №1
# 100 loops, best of 3: 0.031 usec per loop - ВАРИАНТ №2
# 100 loops, best of 3: 0.0501 usec per loop - ВАРИАНТ №3

# Массив из 18 элементов
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №1
# 100 loops, best of 3: 0.0286 usec per loop - ВАРИАНТ №2
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №3

# Анализ с помощью модуля timeit показал, что 
# для массива не больше 3 элементов оптимально использовать ВАРИАНТ №2
# для массива больше 9 элементов оптимально использовать ВАРИАНТ №2
# для массива больше 10 элементов результаты у всех трех ВАРИАНТОВ прибризительно равны