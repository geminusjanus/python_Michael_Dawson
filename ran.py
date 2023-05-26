import random

num = random.randint(1,100)
guess = int(input("Ваше предположение "))
tries = 1

while tries <= 4:
    if guess > num:
        print("Меньше...")
        guess = int(input("Ваше предположение "))
    elif guess < num:
        print("Больше...")
        guess = int(input("Ваше предположение "))
    elif guess == num:
        print("Вам удалось отгадать число! Это в самом деле", num)
        print("Вы затратили на отгадывание", tries, "попыток!\n")
    # guess = int(input("Ваше предположение "))
    tries += 1
print("\nВам не удалось отгадать число")

# print("Вам удалось отгадать число! Это в самом деле", num)
# print("Вы затратили на отгадывание", tries, "попыток!\n")
input("\n\nНажмите Enter чтобы выйти.")