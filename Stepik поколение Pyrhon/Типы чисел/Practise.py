# S,V1,V2=float(input()),float(input()),float(input())
# print(S/(V1+V2))
#
# print((5/9)*((float(input()))-32))

# x=float(input())
# y=(x-int(x))*10
# print(int(y))

# print(input().split('.')[1][0])
# list=[]
# a=0
# while a!=5:
#     list.append(int(input()))
#     a+=1
#
# print(f"Наименьшее число = {min(list)}\nНаибольшее число = {max(list)}")

# nums=[int(input())for i in range(3)]
# x=nums.sort(reverse=True)
# print(x)
# nums = [int(input()) for i in range(3)]
# x = sorted(nums, reverse=True)
# for i in x:
#     print (i)

# l=list(map(int,input()))
# if max(l)-min(l)==sum(l)-(max(l)+min(l)):
#     print("Число интересное")
# else:
#     print("Число неинтересное")

# suma=0
# a=0
# while a!=5:
#     suma+=abs(float(input()))
#     a+=1
# print(sum a)

# lst = map(float, [input() for _ in range(5)])
# # lst = float, [input() for _ in range(5)]
# print(list(lst))

list=[int(input()) for i in range (4)]
print(abs(list[0]-list[2])+abs(list[1]-list[3]))