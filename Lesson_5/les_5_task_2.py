#!/usr/bin/python3
# coding: utf-8

# Интерактивный курс Алгоритмы и структуры данных - GeekUniversity
# Урок 5 Задание 2
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для
# преобразования систем счисления, задача решается в несколько строк.
# Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной
# системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

import collections
from collections import deque  # Используем при подсчете произведения

# Сделано не полностью
## Вариант №1
a = int(162)
b = int(3151)
c = int(a + b)
d = int(a * b)
print('*' * 50)
print(' Сложение 16-х чисел = ', collections.deque(format(c, 'x')), '\n', 'Умножение 16-х чисел = ', collections.deque(format(d, 'x')))

## Вариант №2
# Считаем пользователя идеальным и вводящим данные без ошибок
num1 = list(input('Укажите первое шестнадцатеричное число: ').upper())
num2 = list(input('Укажите второе шестнадцатеричное число: ').upper())

digits_list_16 = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']


# СУММА:
def sum16(a, b):
    if len(a) < len(b):
        a, b = b, a
    # Переворачиваем оба числа:
    a = a[::-1]
    b = b[::-1]
    # Идем циклом по меньшему числу:
    k = 0
    c = []
    for i in range(len(b)):
        d_a = digits_list_16.index(a[i])
        d_b = digits_list_16.index(b[i])
        res = d_a + d_b + k
        if res >= 16:
            k = 1
            res = res % 16
        else:
            k = 0
        c.append(digits_list_16[res])
    # Добавим оставшиеся разряды большего числа
    a_ost = a[len(b):]
    for el in a_ost:
        res2 = digits_list_16.index(el) + k
        if res2 >= 16:
            k = 1
            res2 = res2 % 16
        else:
            k = 0
        c.append(digits_list_16[res2])
    return c[::-1]


# ПРОИЗВЕДЕНИЕ:
def mult16(a, b):
    if len(a) < len(b):
        a, b = b, a
    # Переворачиваем оба числа:
    a = a[::-1]
    b = b[::-1]
    d = []
    for j in range(len(b)):
        k = 0
        d_cur = ['0'] * j
        d_b = digits_list_16.index(b[j])
        for i in range(len(a)):
            d_a = digits_list_16.index(a[i])
            res = d_a * d_b + k
            if res >= 16:
                while res >= 16:
                    k = res // 16
                    res = res % 16
            else:
                k = 0
            d_cur.append(digits_list_16[res])
        d_cur.append(digits_list_16[k])
        d.append(d_cur[::-1])
    deq = deque(d)
    pr = sum16(deq.popleft(), deq.popleft())
    while len(deq) > 0:
        pr = sum16(pr, deq.popleft())
    return pr


num_16_sum = sum16(num1, num2)
num_16_mult = mult16(num1, num2)

print(f'____________________________________________________')
print(f'a = {"".join(num1)}')
print(f'b = {"".join(num2)}')
print(f'a + b = {"".join(num_16_sum)} (как массив: {num_16_sum})')
print(f'a * b = {"".join(num_16_mult)} (как массив: {num_16_mult})')

