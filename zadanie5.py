# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
f1 = open ('text1.txt', 'r')
f2 = open ('text2.txt', 'r')
f3 = open ('text3.txt', 'w')
str1 = f1.read()
str2 = f2.read()
f1.close()
f2.close()
print (f" Исходная строка из файла 1: ", str1)
print (f" Исходная строка из файла 2: ", str2)
max = 0
if (len (str1) > len (str2)):
    max = len (str1)
else:
    max = len (str2)
max_degree =0
if (int (str1[4]) > int (str2[4])):
    max_degree = int (str1[4])
else:
    max_degree = int (str2[4])
print (f"Максимальная степень уравнения = ", max_degree)
list1 = []
for i in range (max_degree+1):
    list1.append(0)
for i in range (4, len(str1), 8):
    list1[int (str1[i])] = int (str1[i-4])
for i in range (4, len(str2), 8):
    list1[int (str2[i])] += int (str2[i-4])
print (f"Коэффициенты при уравнениях", list1)
str3 = str (list1[max_degree]) + "*x^" + str (max_degree)
for i in range (max_degree):
    str3 = str3 + "+" + str (list1[max_degree-1-i]) + "*x^" + str (max_degree-1-i)
print (str3)
f3.write (str3)
f3.close()
# for i in range 