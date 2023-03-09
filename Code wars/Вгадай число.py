from random import randint

num = randint(1, 10)
print(num)
player = 0
while True:
    print("Вгадай число в 1 до 10 ,введи ЦІЛЕ число")
    player = input("Тож твоє число...:")
    print(f"Ти ввів  {player}")
    if "." in player:
        print("Ну ціле число ж треба було , а не з крапкою")
        break
    if player.isalpha():
        print("Мен , треба число а не літери, запускай по новій")
        break
    if int(player) > 10 or int(player) < 0:
        print("Не вписався в діапазон цифр, запускай по новій")
        break
    if int(player) == num:
        print("Вітаю ти вгадав")
        break
    else:
        print("Спробуй ще раз")
