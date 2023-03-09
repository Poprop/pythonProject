# n = input()
# while n!="КОНЕЦ":
#     print(n)
#     n = input()

# n=input()
# count=0
# while n not in ("стоп", "хватит", "достаточно"):
#    count+=1
#    n=input()
# print(count)

# n=int(input())
# total=0
# while 0<n<=5:
#    if n ==5:
#       total+=1
#    n=int(input())
# print(total)

# n=int(input())
# total=0
# while n>=25:
#    n-=25
#    total+=1
# while 10<=n<25:
#    n-=10
#    total+=1
# while 5<=n<10:
#    n-=5
#    total+=1
# while 1<=n<5:
#       n-=1
#       total+=1
# print(total)

# num = "5086334"
# # while num!=0:
# #     print(num%10)
# #     num=num//10
# [print(i,end="")  for i in num [::-1]]

# x=26670
# max=0
# min=9
# while x!=0:
#     b=x%10
#     if b>max:
#         max=b
#     if b<min:
#         min=b
#     x=x//10
# print(max)
# print(min)

# x=list(map(int,input()))
# mnoj=1
# print(sum(x))
# print(len(x))
# for el in x:
#     mnoj*=el
# print(mnoj)
# print(sum(x)/len(x))
# print(x[0])
# print(x[0]+x[-1])

# x=455672
#
# while x>99:
#   x=x//10
# print(x%10)
# x=list(map(int,input()))
# print(x[1])

# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)


# num = int(input())
# res = 0
# n = 2
# while True:
#     if num % n == 0:
#         res = n
#         print(res)
#         break
#     elif num % n != 0:
#         n += 1


# n = int(input())
# limit=[*range(5,10),*range(17,38),*range(78,88)]
# for i in range(1, n + 1):
#     if (
#             i not in range(5, 10) and
#             i not in range(17, 38) and
#             i not in range(78, 88)
#     ):
#         print(i)


# n = int(input())
# limit = [*range(5, 10), *range(17, 38), *range(78, 88)]
# for i in range(1, n + 1):
#     if i not in limit:
#         print(i)
# name,year,description,oscar=input("Веди назву фільму:"),int(input("Рік фільму:")),input("Введи короткий опис:"),input("Чи має фільм оскар:")
# print(name.upper())
# print(description.count(","))
# print(description.find("перший"))
# print(name.split())

name,year,description,oscar=input("Веди назву фільму:"),input("Рік фільму:"),input("Введи короткий опис:"),bool(input(f"Чи має фільм оскар:"))
print(type(name),type(year),type(description),type(oscar),sep="\n")