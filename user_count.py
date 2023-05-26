import random

numFirst = int(input("Введите начало счета: "))
numSecond = int(input("Введите конец счета: "))
numSplit = int(input("Введите интервал счета: "))

for x in range(numFirst, numSecond, numSplit):
    print(x, end=" ")

input("\n\nНажмите Enter чтобы выйти")