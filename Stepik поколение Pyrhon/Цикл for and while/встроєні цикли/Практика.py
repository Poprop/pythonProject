#
# n=int(input())
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()   #виводить кожен стовпчик новий ітерації і в новий рядок

# n=int(input())
# for i in range(1,n+1): #кількість рядків
#     for j in range(5): #кількість елементів в рядку
#         print(i,end=' ') #виведення елементів з розділенням
#     print()             #виведення нового рядка
#
# [print(f'{i} ' * 5) for i in range(1, int(input()) + 1)]

# n=int(input())
# for i in range(1,n+1):
#     print(" ")
#     for j in range(1,10):
#         print(f"{i} + {j} = {i+j}")
#
# a=int(input())
#
# [[print(f'{j} + {i} = {j+i}') for i in range(1,10)]and print() for j in range(1,a+1)]


# n=int(input())
# for i in range(n//2+2):
#         print("*"*i,end="\n")
# for j in range(n//2,0,-1):
#     print("*" * j, end="\n")

# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end='')
#     print()

# total = 0
# for x in range(1, 45):
#     for y in range(1, 45):
#         for z in range(1, 45):
#             if x ** 2 + y ** 2 + z ** 2 == 2020:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)


# for n in range(1,14):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if 28*n+30*k+31*m==365:
#                 print(f"n={n},k={k},m={m} ")
# n=5
# num=0
# for row in range(1,n+1):
#     for j in range(1,row+1):
#         num += 1
#         print(num,end=" ")
#     print()


# n=5
# for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end=" ")
#         for k in range(i-1,0,-1):
#             print(k,end=' ')
#
#         print()
#
# >>>1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

# a = int(input())
# n = int(input())
# num_with_max_dividors = 0
# max_sum_divider = 0
# for x in range(a, n + 1):
#     max_sum_divider_in_iter = 0
#
#     for i in range(1, x + 1):
#         if x % i == 0:
#             max_sum_divider_in_iter += i
#     if max_sum_divider_in_iter >= max_sum_divider:
#         max_sum_divider = max_sum_divider_in_iter
#         num_with_max_dividors = x
# print(num_with_max_dividors, max_sum_divider, sep=" ")
#

# n = int(input())
# for i in range(1, n + 1):
#     plus = 0
#     for k in range(1, i + 1):
#         if i % k == 0:
#             plus += 1
#     print(i,"+" * plus, end='',sep='')
#
#     print()
#

# n=10
# result=0
# j_res = 1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         j_res*=j
#     result+=j_res
#     j_res=1
# print(result)


# Виведення натуральних чисел
# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i)

