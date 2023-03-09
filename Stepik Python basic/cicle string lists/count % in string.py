# x = input()
# x = x.lower()
# nuc_count = 0
# for i in x:
#  if i=="c" or i=="g" in x:
#     nuc_count += 1
# print((nuc_count/len(x))*100)


x = input()
x = x.lower()
percenteg =(((x.count("g")+x.count("c"))/len(x))*100)
print(percenteg)

