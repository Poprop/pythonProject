# x, y = input(), input()
# new_x = ord(x[0]) + int(x[1])
# new_y = ord(y[0]) + int(y[1])
#
# if (new_y + new_x) % 2 == 0:
#     print("YES")
# else:
#     print("NO")

# print(('YES', 'NO')[sum(map(ord, input() + input())) % 2])

print(sum(map(ord, input() + input())))