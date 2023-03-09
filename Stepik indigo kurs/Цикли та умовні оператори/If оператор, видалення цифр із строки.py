# a = list(map(int, input().split()))
# if 3 in a:
#     a.remove(3)
# if 5 in a:
#     a.remove(5)
# if 7 in a:
#     a.remove(7)
# if 9 in a:
#     a.remove(9)
# print(a)

x=input().split()
y=[]
for [i] in x:
    if [i] not in ["3","5","7","9"]:
          y+=[i]
print(y)