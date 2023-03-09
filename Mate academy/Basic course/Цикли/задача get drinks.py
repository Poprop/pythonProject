#number_of_guests = 10
#total_guests = 0
#for i in range(0, number_of_guests + 1):
#    total_guests += i
#print(total_guests)

def get_drinks(number_of_guests: int) -> int:
    total_guests = 0
    for i in range(0, number_of_guests + 1,-1):
        total_guests += i
    return total_guests

print(get_drinks(10))
