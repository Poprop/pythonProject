list = list(map(int, input()))

while len(list) < 6:
    list.insert(0, 0)

if sum(list[0:3]) == sum(list[3:]):
    print("YES")
else:
    print("NO")
