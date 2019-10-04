#!/usr/bin/python3
# coding: utf-8
from random import random

# В программе генерируется случайное целое число от 0 до 100. 
# Пользователь должен его отгадать не более чем за 10 попыток. 
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано. 
# Если за 10 попыток число не отгадано, вывести ответ.

n = round(random() * 100)
i = 1
print('Компьютер загадал число. Отгадайте его. У вас 10 попыток')
while i <= 10:
    u = int(input(str(i) + '-я попытка: '))
    if u > n:
        print('Много')
    elif u < n:
        print('Мало')
    else:
        print('Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано', n)