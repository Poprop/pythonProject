def is_sorted(box_numbers: list) -> bool:
    for i in range(len(box_numbers) - 1):
        if box_numbers[i] < box_numbers[i + 1]:
            return False
    return True


is_sorted([1, 2, 3, 4, 5])
is_sorted([1, 11, 2])

# def is_sorted(lst, key=lambda x: x):
#     for i, el in enumerate(lst[1:]):
#         if key(el) < key(lst[i]): # i is the index of the previous element
#             return False
#     return True
#
