# 5'. Реализуйте алгоритм перемешивания списка.

# было
from os import system
from random import shuffle
from random import randint
system("cls")
print("Реализуйте алгоритм перемешивания списка.")
print("Напечатайте список через пробел: ")
new_list = list(map(int, input().split()))
for i in range(len(new_list)-1):
    n = randint(0, len(new_list)-1)
    new_list[i], new_list[n] = new_list[n], new_list[i]
print(f"Перемешаный список: {new_list}")

# стало
import random 
a = [i * i for i in range(10)]
print(a)
random.shuffle(a)
print(a)



# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Пример:
# 4, 5 -> 20
# # 4,6 -> 12
# # math.gcd(30, 18)

# было
a = int (input("Введите число a: "))
b = int (input("Введите число b: "))
mass = [a, b]
temp_ostatok = max(mass) % min(mass)
temp_min = min(mass)
while temp_ostatok != 0:
    temp_ostatok_while = temp_min % temp_ostatok
    temp_min = temp_ostatok
    temp_ostatok = temp_ostatok_while
print(f"НОД: {temp_min}")
print(f"НОК: {a * b // temp_min}")

# стало
import sympy as sp
a = int (input("Введите число a: "))
b = int (input("Введите число b: "))
print(f"НОК чисел {a} и {b} = {sp.lcm(a, b)}")



# 3 Напишите программу, удаляющую из текста все слова, содержащие "абв".
# *' 'абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'

# было
txt = 'абвгд гдежз жзе абв ыопыпт'
iskom_txt = "абв"
stroka = [i for i in txt.split() if iskom_txt not in i]
print(f'Результат: {" ".join(stroka)}')

# стало
del_st = lambda x, y: " ".join([i for i in x.split() if y not in i])
print(del_st('абвгд гдежз жзе абв  ыопыпт', 'абв'))