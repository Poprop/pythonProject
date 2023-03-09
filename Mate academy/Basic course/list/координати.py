# coordinates = [0, 0]


# def get_location(coordinates: list, commands: list):
#
#
# x = coordinates[0]
# y = coordinates[1]
# count = 0
#
# while len(commands) > count:
#
#     if ('forward' in commands):
#         y += 1
#         if ('back' in commands):
#             y -= 1
#             if ('right' in commands):
#                 x += 1
#                 if ('left' in commands):
#                     x -= 1
#
# count += 1
# get_location([0, 0], ["forward", "right"])

# count += 1


#
# forward= y +1
# back= y - 1
# right= x + 1
# left= x

def getLocation(coordinates, commands):
    dictionary = {
        'forward': (0, 1),
        'back': (0, -1),
        'left': (-1, 0),
        'right': (1, 0)
    }

    for command in commands:
        data = dictionary.get(command, (0, 0))
        coordinates = [coordinates[0] + data[0], coordinates[1] + data[1]]

    return coordinates