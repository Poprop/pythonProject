a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if b1 < a2 or b2 < a1:
    print('пустое множество')
else:
    if a1 > a2:
        a2 = a1
    if b1 > b2:
        b1 = b2
    if a2 == b1:
        print(a2)
    else:
        print(a2, b1)


# a1,b1=int(input()),int(input())
# a2,b2=int(input()),int(input())
# if (b1<a2) or (b2<a1):
#     print("пустое множество")
# elif b1==a2:
#     print(a2)
# elif b2==a1:
#     print(b2)
# elif b1<b2 and a1<a2:
#     print(a2,b1)
# elif a2<a1 and b2<b1:
#      print(a1,b2)
# elif a1==a2 and b1<b2:
#     print(a1,b1)
# elif b1==b2 and a1>a2:
#     print(a1,b1)
# elif a1>a2 and b1<b2:
#     print(a1,b1)
# elif a2>a1 and b2<b1:
#     print(a2,b2)
# elif a1<a2 and b1==b2:
#     print(a2,b2)
# elif a1==a2 and b2<b1:
#     print(a2,b2)
# elif a1==a2 and b1==b2:
#     print(a1,b1)