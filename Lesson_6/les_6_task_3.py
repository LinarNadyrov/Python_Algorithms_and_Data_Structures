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

''' В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться. '''

import sys
from random import random

count = int(input('Введите размер массива: '))
array = [0] * count
for i in range(count):
    array[i] = int(random() * 100)
print(array)

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
print(sys.getsizeof(array[pos1]))
print(sys.getsizeof(array[pos2]))

## ВАРИАНТ №2
min1 = min(array)
array.remove(min1)
min2 = min(array)
if min1 == min2:
    print('Наименьшее число: ', min1)
else: 
    print('Два наименьших числа: ', min1, ' и ', min2)
print(sys.getsizeof(min1))
print(sys.getsizeof(min2))


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
print(sys.getsizeof(array[min1]), 'и', sys.getsizeof(array[min2]))

# 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
# [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] darwin

# Во всех вариантах выделеной памяти = 56 байтов