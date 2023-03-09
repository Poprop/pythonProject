# def modify_list(l):
#
#
# d = []
# for el in l:
#     if el % 2 != 0:
#         l.remove(el)
#     if el % 2 == 0:
#         el //= 2
#         d.insert(el)
#         print(d)
#
# print(modify_list([1, 2, 3, 4, 5, 6]))

# def modify_list(l):
l = [1, 2, 3, 4, 5, 6]


# def modify_list(l):
#
#
#     for i in range(len(l) - 1, -1, -1):
#         if l[i] % 2 != 0:
#             del l[i]
#         else:
#             l[i] = l[i] // 2


def modify_list(l):

  l[:]= [int(num//2) for num in l if num %2==0]