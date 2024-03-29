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


# Вводятся три разных числа. 
# Найти, какое из них является средним (больше одного, но меньше другого).

import timeit
import cProfile
## ВАРИАНТ №1
def average_number1(a, b, c): 
    if b < a < c or c < a < b: 
        return print('среднее число:', a) 
    elif a < b < c or c < b < a:
        return print('среднее число:', b)
    else: 
        return print('среднее число:', c)

## ВАРИАНТ №2
def average_number2(a, b, c): 
    if b > a and a > c or c > a and a > b:
        return print('среднее число:', a) 
    if a > b and b > c or c > b and b > a: 
        return print('среднее число:', b)
    if a > c and c > b or b > c and c > a: 
        return print('среднее число:', c)


print ('Введите пожалуйста три числа а b c : ')
a = int(input())
b = int(input())
c = int(input())
average_number1(a, b, c)
#average_number2(a, b, c)

## ВАРИАНТ №3
arr = []  # заводим пустой список
n = 3     # длина массива
print ('Введите пожалуйста три числа а b c : ')
for i in range(n):  
    arr.append(int(input()))
print(arr)
arr = sorted(arr)
if arr[1] != max(arr) and arr[1] != min(arr):
    print('среднее число:', arr[1])
else: 
    print('среднее число:', arr[1])

#average_number(a, b, c)
#cProfile.run('average_number(1585, 1595, 1599)')

# Тест с помощью timeit 
# Тест на числах 1 2 3 
# 100 loops, best of 3: 0.0405 usec per loop - ВАРИАНТ №1
# 100 loops, best of 3: 0.0215 usec per loop - ВАРИАНТ №2
# 100 loops, best of 3: 0.0381 usec per loop - ВАРИАНТ №3

# Тест на числах 85 95 99
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №1
# 100 loops, best of 3: 0.031 usec per loop - ВАРИАНТ №2
# 100 loops, best of 3: 0.0501 usec per loop - ВАРИАНТ №3

# Тест на числах 585 595 599
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №1
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №2
# 100 loops, best of 3: 0.0405 usec per loop - ВАРИАНТ №3

# Тест на числах 1585 1595 1599
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №1
# 100 loops, best of 3: 0.0405 usec per loop - ВАРИАНТ №2
# 100 loops, best of 3: 0.0477 usec per loop - ВАРИАНТ №3

# Тест с помощью cProfile 
# Данные варианта №1, №2 и №3 совпадают
# Во всех заданных параметрах время выполнения одинаково

# среднее число: 1595
#          5 function calls in 0.000 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:13(average_number)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Общий вывод
# Анализ с помощью модуля timeit показал, что 
# для чисел => xx оптимально использовать ВАРИАНТ №1 
# для чисел = x оптимально использовать ВАРИАНТ №2

# Анализ с помощью модуля cProfile показал, что скорость работы всех ВАРИАНТОВ равны (различий нет).