# black = ["a1", "c1", "e1", "g1", "b2", "d2", "f2", "h2", "a3", "c3", "e3", "g3", "d4", "b4", "f4", "h4", "a5", "c5",
#          "e5", "g5", "b6", "d6", "f6", "h6", "a7", "c7", "e7", "g7", "b8", "d8", "f8", "h8"]
#
# x, y = input(), input()
#
# if x or y not in black:
#     print("NO")
# else:
#     print("YES")

#
# x, y = input(), input()
# new_x = ord(x[0]) + int(x[1])
# new_y = ord(y[0]) + int(y[1])
#
# if (new_y + new_x) % 2 == 0:
#     print("YES")
# else:
#     print("NO")

# n=[2,3,4,5,4]
# count=0
# if len(n)==1:
#     print("Jumping")
# for el in range(len(n)-1):
#     if n[el]-n[el+1]!=1 or n[el]-n[el+1]!=-1:
#         count += 1
# if count>1:
#     print("not")
# else:
#     print("Jumping")

# x=input()
# print("YES" if x.istitle()==True else "NO")
# x=str(input())
# print("YES" if "хорош" in x.lower() else "NO")
# x="gggggggg1212321ABDCEFCE"
# count=0
# for el in x:
#     if el.islower()==True:
#         count+=1
# print(count)

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
