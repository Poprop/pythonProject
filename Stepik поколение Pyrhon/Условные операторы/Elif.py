# n,k=int(input()),int(input())
# print("NO" if n>k else "YES" if k>n  else "Don't know")

# print((lambda zoom, b: ["NO", "YES", "Don't know", ][(zoom <= b) + (zoom == b)])(int(input(), int(input()))))
# print((lambda a, b: ["NO", "YES", "Don't know"][(a <= b) + (a == b)])(int(input()), int(input())))
# print((lambda a,b,c: ["Разносторонний","Равнобедренный",'Равносторонний'][(a==b or a==c or c==b)+(a==b==c)])(int(input()),int(input()),int(input())))

# a,b,c=int(input()),int(input()),int(input())
# if a<b<c or c<b<a:
#     print(b)
# elif b<a<c or c<a<b:
#     print(a)
# elif a<c<b or b<c<a:
#     print(c)

# x=int(input())
# thirty_one=1, 3, 5, 7, 8, 10, 12
# thirty=4, 6, 9, 11
# twenty=2
# print("31" if x in thirty_one else "30" if x in thirty else "28")
#
# print([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][int(input())-1])
# x=int(input())
# print("Легкий вес" if x<60 else "Первый полусредний вес" if 60<=x<64 else "Полусредний вес" )
#
# x = int(input())
# if 1 <= x <= 10:
#     if x % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# if 11 <= x <= 18:
#     if x % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# if 19 <= x <= 28:
#     if x % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# if 29 <= x <= 36:
#     if x % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# if x == 0:
#     print("зеленый")
# if x<0 or x>36:
#     print("ошибка ввода")


a1,b1=int(input()),int(input())
a2,b2=int(input()),int(input())
if (b1<a2) or (b2<a1):
    print("пустое множество")
elif b1==a2:
    print(a2)
elif b2==a1:
    print(b2)
elif b1<b2 and a1<a2:
    print(a2,b1)
elif a2<a1 and b2<b1:
     print(a1,b2)
elif a1==a2 and b1<b2:
    print(a1,b1)
elif b1==b2 and a1>a2:
    print(a1,b1)
elif a1>a2 and b1<b2:
    print(a1,b1)
elif a2>a1 and b2<b1:
    print(a2,b2)
elif a1<a2 and b1==b2:
    print(a2,b2)
elif a1==a2 and b2<b1:
    print(a2,b2)
elif a1==a2 and b1==b2:
    print(a1,b1)