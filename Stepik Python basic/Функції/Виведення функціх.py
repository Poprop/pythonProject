def f(x):
    if x <= -2:
        return 1 - ((x + 2) ** 2)
    if -2 <= x <= 2:
        return -(x / 2)
    if 2<x:
        return((x-2)**2)+1
print(f(1))



f= lambda x:1 - ((x + 2) ** 2) if x <= -2 else -(x / 2) if -2 <= x <= 2 else ((x-2)**2)+1
