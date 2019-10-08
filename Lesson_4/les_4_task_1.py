#!/usr/bin/python3
# coding: utf-8
# Вводятся три разных числа. 
# Найти, какое из них является средним (больше одного, но меньше другого).

import timeit
import cProfile
## ВАРИАНТ №1
# def average_number(a, b, c): 
#     if b < a < c or c < a < b: 
#         return print('среднее число:', a) 
#     elif a < b < c or c < b < a:
#         return print('среднее число:', b)
#     else: 
#         return print('среднее число:', c)

## ВАРИАНТ №2
# def average_number(a, b, c): 
#     if b > a and a > c or c > a and a > b:
#         return print('среднее число:', a) 
#     if a > b and b > c or c > b and b > a: 
#         return print('среднее число:', b)
#     if a > c and c > b or b > c and c > a: 
#         return print('среднее число:', c)


# print ('Введите пожалуйста три числа а b c : ')
# a = int(input())
# b = int(input())
# c = int(input())

arr = []  # заводим пустой список
n = 3
print ('Введите пожалуйста три числа а b c : ')
for i in range(n):  
    arr.append(int(input()))
print(arr)
#print(arr[1])
if arr[1] != max(arr) and arr[1] != min(arr):
    print('среднее число:', arr[1])
else: 
    print()

#average_number(a, b, c)
#cProfile.run('average_number(1585, 1595, 1599)')

# if b > a and a > c or c > a and a > b:
#     print('среднее число:', a) 
# if a > b and b > c or c > b and b > a: 
#     print('среднее число:', b)
# if a > c and c > b or b > c and c > a: 
#     print('среднее число:', c)

# if b < a < c or c < a < b:
#     print('среднее число:', a)
# elif a < b < c or c < b < a:
#     print('среднее число:', b)
# else:
#     print('среднее число:', c) 

# Тест с помощью timeit 
# Тест на числах 1 2 3 
# 100 loops, best of 3: 0.0405 usec per loop - ВАРИАНТ №1
# 100 loops, best of 3: 0.0215 usec per loop - ВАРИАНТ №2

# Тест на числах 85 95 99
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №1
# 100 loops, best of 3: 0.031 usec per loop - ВАРИАНТ №2

# Тест на числах 585 595 599
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №1
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №2

# Тест на числах 1585 1595 1599
# 100 loops, best of 3: 0.0191 usec per loop - ВАРИАНТ №1
# 100 loops, best of 3: 0.0405 usec per loop - ВАРИАНТ №2

# Тест с помощью cProfile 
# Данные варианта №1 и №2 совпадают
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