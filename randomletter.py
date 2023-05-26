import random

word = "индекс"
print("В переменной word хранится слово: ", word, "\n")
high = len(word)
low = -len(word)
for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
input("\n\nНажмите Enter чтобы выйти")