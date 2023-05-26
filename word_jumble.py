import random

WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")

word = random.choice(WORDS)

clues = 0

if word == WORDS[0]:
    clues = "Змеиный язык программирования"
elif word == WORDS[1]:
    clues = "Слово или словосочетание, образованное путём перестановки букв"
elif word == WORDS[2]:
    clues = "Легко"
elif word == WORDS[3]:
    clues = "Тяжело"
elif word == WORDS[4]:
    clues = "Отвечают на вопрос"
elif word == WORDS[5]:
    clues = "Подставка для стакана"

counter = 0

correct = word

jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(jumble)

guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != "":
    print("К сожалению, не сходится")
    clue = input("Хотите подсказку? Если да нажмите Y. Если нет нажмите N: ")
    if clue == "y":
        print(f"Подсказка: {clues}")
        counter -= 2
        guess = input("Попробуйте еще раз: ")
    elif clue == "n":
        guess = input("Попробуйте еще раз: ")
    else:
        print("Неверный ввод")

if guess == correct:
    print ("Вы отгадали")
    counter += 10
    print("Вы набрали: ", counter)


input("\n\nНажмите Enter чтобы выйти. ")
