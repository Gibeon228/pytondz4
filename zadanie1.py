# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141
import math

k = math.pi
print ("Введите d")
d = input()
k = str (k)


index_k = k.index('.')
index_k = index_k + len(d)-2
k = k[:index_k+1]
print (k)
# str1 = str(k).split(".")
# str_finish = []
# for i in range (len(d)-2):
#     str_finish.append(str1[1][i])
# print (str_finish)
# for i in range (str_finish):

