#!/usr/bin/python3
# coding: utf-8
# Определить, является ли год, который ввел пользователь, високосным или не високосным.

# Вводится год, преобразуется к целому числу
print('Введите пожалуйста год и мы определим является ли он високосным: ')
year = int(input())
print('==============================================', '\n')
# Если остаток от деления на 4 не равен нулю,
# значит год не делится нацело на 4 и
# не является високосным, т. е. он обычный.
if year % 4 != 0:
    print('Год: ', year, 'является не високосным!')
# Исключаем столетия, которые не делятся на 400
elif year % 100 == 0: # является ли столетием?
    if year % 400 == 0: # Делится ли на 400?
        # В таком случае год високосный
        print('Год: ', year, 'високосный :-)')
    else: # Если столетие, но не делится на 400,
        # то год обычный
        print('Год: ', year, 'является не високосным!')
# Во всех остальных случаях год високосный
else:
    print('Год: ', year, 'високосный :-)')
print('==============================================', '\n')