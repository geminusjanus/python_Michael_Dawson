import random


counter = 0
tails = 0
head = 0

while counter <= 99:
    num = random.randint(1,2)
    if num == 1:
        head += 1
        counter += 1
    elif num == 2:
        tails += 1
        counter += 1
print("Столько раз выпадала решка: ", tails, "и столько раз выпадал орел", head)