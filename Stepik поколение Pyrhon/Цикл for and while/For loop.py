# n=int(input())
# for i in range (n,0,-1):
#     print("*"*(n-i))

# [print("i"*i) for i in range(int(input()),0,-1)]

# m,p,n=int(input()),int(input()),int(input())
# for i in range(n):
#     print(i+1,m * (p / 100 +  1) ** i)
#

# m, p, n = int(input()), int(input()) * 0.01 + 1, int(input())
# for i in range(n):
#     print(i + 1, m)
#     m = m * p

# [print(i) for i in range(int(input()),int(input())+1)]
# m,n=int(input()),int(input())
#
# if m>n:
#     for i in range(m,n-1,-1):
#         print(i)
# elif m<n:
#     for i in range(m,n+1):
#         print(i)
# else:
#     print(m)

# m, n = int(input()), int(input())
# if m%2==0:
#     m-=1
# if n%2==0:
#     n-=1
# for i in range(m, n+2,-2):
#     print(i)
#
# m, n = int(input()), int(input())
# for i in range(m,n-1,-1):
#     if i % 2 !=0:
#         print(i)

# m,n=int(input()), int(input())
#
# for i in range (m,n+1):
#     if i%17==0 or i%10==9 or i%15==0:
#         print(i)

# x=int(input())
# [print(f"{x} x {i} = {x*i}") for i in range(1,11)]
#
#
# (lambda n: [print(f'{n} x {i} = {n*i}') for i in range(1, 11)])(int(input()))
# from math import pow
# n=int(input())
# result=0
# for i in range (1,n+1):
#     if pow(i,2)%10==2 or pow(i,2)%10==5 or pow(i,2)%10==8:
#         result+=i
# print(result)


# result=1
# for i in range(1,11):
#     n = int(input())
#     if n!=0:
#         result*=n
# print(result)
# n = int(input())
# res=0
# for i in range (1,n+1):
#     if n%i==0:
#         res+=i
# print(res)

# n=int(input())
# res=0
# for i in range(1,n+1):
#     if i%2==0:
#         res-=i
#     else:
#         res+=i
# print(res)

# n= int(input())
# list=[]
# for i in range(n):
#     list.append(int(input()))
# sor_list=sorted(list)
# print(*(sor_list[-1],sor_list[-2]),sep="\n")
# #list=[]
# count=0
# for i in range(10):
#     n= int(input())
#     if n%2==0:
#         count += 1
#     #list.append(n)
# # for el in range(len(list)):
# #     if list[el]%2==0:
# #         count+=1
# if count==10:
#     print("YES")
# else:
#     print('NO')
#
# flag = "YES"
# for i in range(10):
#     num = int(input())
#     if num % 2 != 0:
#         flag = "NO"
# print(flag)

# f1=1
# f2=1
# #list=[]
# n=int(input())
# if n == 1 :
#     print(n)
# else:
#     for i in range(n):
#        print(f1,end=' ')
#        f1,f2=f2,f1+f2
       #list.append(f2)
#print(*(list),sep=' ')

x1,x2=1,1
n=int(input())
for i in range(n):
    print(x1,end=' ')
    x1,x2=x2,x1+x2
