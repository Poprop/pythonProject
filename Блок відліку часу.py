import time
def fun():
    for x in range(1000000):
        print(x)
start = time.time()

fun()
end = time.time()

total = end - start
print("Program takes", total)