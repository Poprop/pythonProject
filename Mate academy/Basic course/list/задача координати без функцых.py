coordinates = [0, 0]
commands = ["forward", "right"]

x = coordinates[0]
y = coordinates[1]
pre = [x, y]
count = 0

while len(commands) > count:

    if ('forward' in commands):
        y += 1
        if ('back' in commands):
            y -= 1
            if ('right' in commands):
                x += 1
                if ('left' in commands):
                    x -= 1

count += 1
result = [x, y]
print(result)
# get_location([0, 0], ["forward", "right"])
