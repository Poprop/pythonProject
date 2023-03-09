def get_drinks_with_step(number_of_guests: int, step: int) -> int:
    total_guests = 0
    for i in range(0, number_of_guests + 1, step):
        total_guests += i
    return total_guests

print(get_drinks_with_step(10, 1))
print(get_drinks_with_step(10, 2))
print(get_drinks_with_step(10, 3))


