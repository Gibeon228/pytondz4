# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

list1 = [1, 1, 2, 3, 4, 5, 5]
list2 = []
n = len(list1)
i = 0
while (i < n):
    help = 0
    j = i+1
    while (j < n):
        if (list1[i] == list1[j]):
            help = 1
            list1.pop(j)
            n-=1
            j-=1
        j+=1
    if (help == 1):
        list1.pop(i)
        i-=1
        n-=1
        help = 0
    i+=1
print (list1)
        

    


