def build_house(number_of_floors , color):
    house = f'{color} {number_of_floors}-floors house {color}'

    return house
small_house = build_house(2 , 'red')
big_house = build_house(9, 'white')

print(small_house)
print(big_house)