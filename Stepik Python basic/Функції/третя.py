d = {}
for i in range(int(input())):
    x = int(input())
    if x not in d:
        d[x] += f(x)
