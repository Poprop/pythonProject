# x=int(input())
# y=int(input())
# sum=int()
#
# while True:
#     sum+=y
#     if sum%x==0:
#         print(sum)
#         break
#

a=int(input())
b=int(input())
d=a
while d%a!=0 or d%b!=0:
    d+=1
    print(d)
print(d)