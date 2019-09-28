#!/usr/bin/python3
# coding: utf-8
# Вводятся три разных числа. 
# Найти, какое из них является средним (больше одного, но меньше другого).

print ('Введите пожалуйста три числа а b c : ')
a = int(input())
b = int(input())
c = int(input())
if b < a < c or c < a < b:
    print('среднее число:', a)
elif a < b < c or c < b < a:
    print('среднее число:', b)
else:
    print('среднее число:', c)