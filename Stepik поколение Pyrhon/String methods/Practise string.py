# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# print(s.find("w"))

# print(*input()[::2],sep="\n")

# x=input()
# for el in range(len(x)):
#     if el%2==0:
#        print(x[el])

# [print (i) for i in input()[::-1]]
# print(*input()[::-1],sep="\n")
# ________________________________
# a,b,c=input(),input(),input()
# print(b[0],a[0],c[0],sep='')
#
# s = [input()[0] for _ in range(3)]
# print(s[1], s[0], s[2], sep='')
# ---------------------------------

# x=input()
# summa=0
# for el in range(len(x)):
#     summa+=x[el]
# print(summa)
# s=[input()]

# x="Hi Python"
# count=0
# for i in range(len(x)):
#     if x[i] in "123456789":
#         count+=1
# if count>0:
#     print('Цифра')
# else:
#     print('Цифр нет')
#     або
# print('Цифра' if any(map(str.isdigit, input())) else 'Цифр нет')

# s=input()
# count_star=0
# count_plus=0
# for i in s:
#     if i=="*":
#         count_star +=1
#     if i=="+":
#         count_plus +=1
# print(f"Символ + встречается {count_plus} раз")
# print(f"Символ * встречается {count_star} раз")

# n=input()
# count=0
# perm=""
# for el in range(len(n)-1):
#     if n[el]==n[el+1]:
#         count+=1
# print(count)

# n=input().lower()
# wowels="ауоыиэяюёе"
# not_wowels="бвгджзйклмнпрстфхцчшщ"
# wow_count=0
# not_w_count=0
# for i in range(len(n)-1):
#     if n[i] in wowels:
#         wow_count+=1
#     elif n[i] in not_wowels:
#         not_w_count+=1
# print(f"Количество гласных букв равно {wow_count}")
# print(f"Количество согласных букв равно {not_w_count}")

# n=int(input())
# p=""
# while n!=0:
#     p+=str(n%2)
#     n=n//2
# print(p[::-1])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-9:])

# n=input()
# if n==n[::-1]:
#     print("YES")
# else:
# #     print("NO")
# n=input()
# print("YES" if n==n[::-1] else "NO")
#
# n="abcdefghijklmnopqrstuvwxyz"
# print(len(n),n*3,n[0],n[:4],n[-3:],n[::-1],
#       n[1:-2],sep="\n")
# n=input()
# print(n[2],n[-2],n[:6],n[:-2],n[::2],n[::1],n[::-1],n[-1::-2],sep="\n")

# n="abcdefg"
# d=len(n)//2
# if len(n)%2==0:
#     print(n[d:]+n[:d])
# else:
#     print(n[d+1:]+n[:d+1])

# n=input()
# most=""
# count=0
# for el in n:
#     count_el=n.count(el)
#     if count_el>=count:
#         count=count_el
#         most=el
# print(most,count)

# n = "abfcdefg"
# if "f" not in n:
#     print("NO")
# if n.count("f") == 1:
#     print(n.find("f"))
# if n.count("f") > 1:
#     print(n.find("f"), n.rfind("f"), sep=" ")

# n="ahahahahaha"
# print(n[:n.find("h")],n[n.rfind("h")+1:],sep="")

# age = 27
# name = 'Timur'
# profession = 'math teacher'
# txt = 'My name is {}, I am {}, I work as a {}'.format(name, age, profession)
# print(txt)
# s = 'In {0}, someone paid {1} {2} for two pizzas.'
# year,ammount,cript=2010,"10k","Bitcoin"
# print(s.format(year,ammount,cript))

print('In {0}, someone paid {1} {2} for two pizzas.'.format(2010,"10k","Bitcoin"))
