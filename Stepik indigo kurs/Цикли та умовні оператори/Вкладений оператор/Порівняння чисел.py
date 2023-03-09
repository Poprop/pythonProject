# a = int(input())
# b = int(input())
# if a < b:
#     print("<")
# if a > b:
#     print(">")
# if a == b:
#     print("=")
#
# print("<" if (a:=int(input()))<(b:=int(input())) else ">" if a>b else "=")
#
#
# ___________________________________________________________________________
#
a = int(input())
b = int(input())
c = int(input())

print(a if a>b and a>c else b if b>a and b>c else c )

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)