#
# from math import *
# x1,y1=float(input()),float(input())
# x2,y2=float(input()),float(input())
# quadr=pow((x1-x2),2)+pow((y1-y2),2)
# rad=sqrt(quadr)
# print(quadr)
# print(rad)
# from math import sqrt
# x1=float(input())
# y1=float(input())
# x2=float(input())
# y2=float(input())
# x=pow(x1-x2,2)
# y=pow(y1-y2,2)
# print(sqrt(x+y))

# from math import pi,pow
# r=float(input())
# print(pi*pow(r,2))
# print(2*pi*r)

# from math import sqrt
# a,b=float(input()),float(input())
# print((a+b)/2)
# print(sqrt(a*b))
# print((2*a*b)/(a+b))
# print(sqrt((a**2+b**2)/2))

# from math import pi,cos,sin,tan
# r=(float(input())*pi)/180
# print(sin(r)+cos(r)+(tan(r)**2))

# from math import floor,ceil
# x=float(input())
# print(ceil(x)+floor(x))
# from math import pow, sqrt, fabs
#
# a, b, c = float(input()), float(input()), float(input()),
# D = pow(b, 2) - 4 * (a * c)
# if D < 0:
#     print("Нет корней")
# elif D > 0:
#     # (((-b)+sqrt(pow(b,2)-4*(a*c)))/2*a ,"\n",((+b)+sqrt(pow(b,2)-4*(a*c)))/2*a,sep="")
#     res1 = ((-b) + sqrt(pow(b, 2) - 4 * (a * c))) / 2 * a
#     res2 = ((+b) + sqrt(pow(b, 2) - 4 * (a * c))) / 2 * a
#     if res1 < res2:
#         print(fabs(res1), "\n", fabs(res2),sep="")
#     else:
#         print(fabs(res2), "\n", fabs(res1),sep="")
# elif D == 0:
#     print(-(b / (2 * a)))


# from math import pow, sqrt, fabs
#
# a, b, c = float(input()), float(input()), float(input()),
# D = pow(b, 2) - 4 * a * c
# if D < 0:
#     print("Нет корней")
# elif D > 0:
#     res1 = ((-b + sqrt(D)) / (2 * a))
#     res2 = ((-b - sqrt(D)) / (2 * a))
#     if res1 < res2:
#          print(res1, "\n", res2,sep="")
#     else:
#         print(res2, "\n", res1,sep="")
# elif D == 0:
#      print(-(b / (2 * a)))
# from math import pow
# n=int(input())
# for i in range(n+1):
#     pow_i=pow(i,2)
#     print(f"Квадрат числа {i} равен {int(pow_i)}")
# print(*[f"Квадрат числа {i} равен {pow(i, 2)}" for i in range(int(input()) + 1)], sep="\n")

