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

# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import timeit
import cProfile
from random import random

count = int(input('Введите размер массива: '))
array = [0] * count
for i in range(count):
    array[i] = int(random() * 100)
print(array)

# def array_size(count):
#     count = int(input('Введите размер массива: '))
#     array = [0] * count
#     for i in range(count):
#         array[i] = int(random() * 100)
#     return array

## ВАРИАНТ №1
pos1 = 0
pos2 = 0
for i, item in enumerate(array):
    if item <= array[pos1]:
        pos2 = pos1
        pos1 = i
    elif item <= array[pos2]:
        pos2 = i
print('Два наименьших числа:', array[pos1], ' и ', array[pos2])

## ВАРИАНТ №2
min1 = min(array)
array.remove(min1)
min2 = min(array)
if min1 == min2:
    print('Наименьшее число: ', min1)
else: 
    print('Два наименьших числа: ', min1, ' и ', min2)

## ВАРИАНТ №3
if array[0] > array[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2,count):
    if array[i] < array[min1]:
        b = min1
        min1 = i
        if array[b] < array[min2]:
            min2 = b
    elif array[i] < array[min2]:
        min2 = i
print('Два наименьших числа: ', array[min1], ' и ', array[min2])

# Тест с помощью timeit 
# Массив из 3 элементов
# 100 loops, best of 3: 0.0405 usec per loop - ВАРИАНТ №1
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №2
# 100 loops, best of 3: 0.031 usec per loop - ВАРИАНТ №3

# Массив из 9 элементов
# 100 loops, best of 3: 0.031 usec per loop - ВАРИАНТ №1
# 100 loops, best of 3: 0.031 usec per loop - ВАРИАНТ №2
# 100 loops, best of 3: 0.031 usec per loop - ВАРИАНТ №3

# Массив из 18 элементов
# 100 loops, best of 3: 0.031 usec per loop - ВАРИАНТ №1
# 100 loops, best of 3: 0.0286 usec per loop - ВАРИАНТ №2
# 100 loops, best of 3: 0.0286 usec per loop - ВАРИАНТ №3

# Анализ с помощью модуля timeit показал, что 
# для массива не больше 3 элементов оптимально использовать ВАРИАНТ №2
# для массива больше 3 элементов результаты у всех трех ВАРИАНТОВ прибризительно равны