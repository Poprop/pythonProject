# Через цикл while
# x=1
# x2=1
# n=(int(input()))
#
# print(x,x2 , end=" ")
# while n>2:
#     x,x2=x2,x+x2
#     print(x2,end=" ")
#     n-=1

# Через цикл for
# x=1
# x2=1
# n=(int(input()))
#
# print(x,x2 , end=" ")
# for i in range(2,n):
#     x, x2 = x2, x + x2
#     print(x2, end=" ")


# x = 1
# x2 = 1
# n = (int(input()))
# if n <=0 :
#     print(0)
# if n == 1:
#     print(1)
#
# for i in range( n):
#     x, x2 = x2, x + x2
# print(x2, end=" ")

# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# f

def main():
x, x2 = 1, 1
n = int(input())
for i in range(n):
    x, x2 = x2, x2 + x
    print(x2)
