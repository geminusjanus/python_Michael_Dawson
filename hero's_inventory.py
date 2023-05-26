inventory = ()
if not inventory:
    print("Вы безоружны")
input("\nНажмите Enter чтобы продолжить")

inventory = ("Меч",
             "Кольчуга",
             "Щит",
             "Эликсир")
print("\nСодержимое кортежа: ")
print(inventory)
print("\nИтак в вашем арсенале: ")

for item in inventory:
    print(item)

print("Сейчас в ващем распоряжении", len(inventory), "предмета/-ов")
input("\nНажмите Enter чтобы продолжить")

if "Эликсир" in inventory:
    print("Вы еще поживете и повоюете")

index = int(input("\nВведите индекс одного из предметов арсенала (0-4) "))
print("Под индексом", index, "в арсенале находится", inventory[index])

start = int(input("\nВведите начальный индекс среза: "))
finish = int(input("Конечная позиция: "))

print("Срез inventory [", start, ":", finish, "] выглядит как", end=" ")
print(inventory[start:finish])

input("\n\nНажмите Enter чтобы продолжить. ")

chest = ("Золото", "Драгоценные камни")
print("Вы нашли ларец. Вот что в нем есть: ")
print(chest)

print("Содержимое лацра помещено в арсенал")

inventory += chest

print("Теперь в вашем распоряжении: ")
print(inventory)

input("\n\nНажмите Enter чтобы выйти. ")