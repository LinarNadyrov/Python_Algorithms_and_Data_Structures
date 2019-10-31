#!/usr/bin/python3
# coding: utf-8
# Сделано не правильно!

''' Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в 
рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным 
использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев 
в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.
Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, 
а проявили творчество, фантазию и создали универсальный код для замера памяти. '''

''' В массиве случайных целых чисел поменять 
местами минимальный и максимальный элементы '''

import sys
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
print(sys.getsizeof(array[i]))

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
print(sys.getsizeof(array[i]))

## ВАРИАНТ №3
array[array.index(max(array))], array[array.index(min(array))] = array[array.index(min(array))], array[array.index(max(array))]
print(array)
print(sys.getsizeof(array))

# 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
# [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] darwin

# В первом и во втором варианте выделено памяти = 28 байт
# В третьем варианте выделено памяти = 88 байт
# Использование алгоритмического метода, потребляет меньше памяти чем стандартные функиции python