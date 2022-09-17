# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: # k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
from random import randint
print("Введите число к")
k = int (input())
list1 =[]
str1 = ""
for i in range (k+1):
    list1.append(str (randint(0, 100)) + "*x ^"+ str (i))
str1 = str1 + list1[k]
for i in range (k):
    str1 = str1 + " + " + list1[k-1-i]
f = open ('text.txt', 'w')
f.write (str1)
f.close()


