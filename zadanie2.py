# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]


print("Введите число N")
n = int (input())
count = 2
simple_mult = []
while (n > 1):
    while (n % count == 0):
        simple_mult.append(count)
        n = n/count
    count+=1
print (simple_mult)

