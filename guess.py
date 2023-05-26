import random

num = int(input("Введите число от 1 до 100, а компьютер должен его отгадать: "))

guess = 0

while num != guess:
    guess = random.randint(1, 100)
    if guess > num:
        guess = random.randint(num, 100)
    elif guess < num:
        guess = random.randint(1, num)
print(guess)
input("\n\nНажмите Enter чтобы выйти")