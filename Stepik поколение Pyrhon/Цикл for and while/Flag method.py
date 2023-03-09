# n = int(input())
# total = 0
# flag = True
# for i in range(1, n + 1):
#     if flag == True:
#         total += i
#         flag = False
#     else:
#         total -= i
#         flag = True
# print(total)
#
# n=int(input())
# res=0
# for i in range(1,n+1):
#     if i%2==0:
#         res-=i
#     else:
#         res+=i
# print(res)

n= int(input())
list=[]
for i in range(n):
    list.append(int(input()))
sor_list=sorted(list)
print(*(sor_list[-1],sor_list[-2]),sep="\n")
