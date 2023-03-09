#a = [int(i) for i in input().split()]
a=[1,3,5,6,1,0]
b = []
n = len(a)
if n < 2:
    b = a
else:
    for i in range(n):
        b.append(a[i - 1] + a[i + 1 - n])

print(*b)