# Задача 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.(Сделать для строки)
# Например:
#     - 6782 -> 23
#     - 0,56 -> 11

n = input('Введите число: ')
sum_digit = 0
for i in n:  # циклом пробегаемся по всей строке
    if i.isdigit():  # проверяем является ли символ цифрой
        # прбавляем число к сумме предварительно приобразовав в целое число
        sum_digit += int(i)
print(f'Сумма цифр числа {n} равна {sum_digit}')

# второй вариант решения
n = input("В ведите число: ")
sum_digit = 0
for i in n:
    if i == ".": # если символ равен точке
        i = 0 # тогда меняем ее на 0
        sum_digit += int(i)
print(f'Сумма цифр числа {n} равна {sum_digit}')
