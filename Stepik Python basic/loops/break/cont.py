while True:
    x = int(input())
    if x<10:
        continue
    if x>100:
        break
    print(x)

#------------------------------
x = 0
while x <= 100:
    if x>9: print(x)
    x = int(input())