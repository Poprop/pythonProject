a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(f" \t\t\t{a}\t\t\t\t{b}")
for i in range(a, b + 1):
    print(f"{i}\t\t\t{c * i}\t\t\t{d * i}")


# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
#
# print('\t', *range(c, d+1), sep='\t')
# for i in range(a,b+1):
#     print(i, *range(i*c,(i*d)+1, i), sep='\t')

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
#
# for i in range(c, d + 1):
#     print("\t" + str(i), end="")
#
# print()
#
# for i in range(a, b + 1):
#      print(i, end="\t")
#      for n in range(c, d + 1):
#          print(i * n, end="\t")
#      print()