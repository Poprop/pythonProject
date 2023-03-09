# numbers = [10, 20, 300, -1, -5, 1]
# min = numbers[0]
#
# for elem in numbers:
#     min = minimun(min, elem)
#
# print(min)


# import math
# def get_speed_statistic(test_results: list) -> list:
#     num_min = test_results[0]
#     num_max = test_results[0]
#     total_num_in_list = 0
#
#     for num in test_results:
#         if num < num_min:
#             num_min = num
#         else:
#             if num > num_max:
#                 num_max = num
#         total_num_in_list += num
#
#
#     return ([num_min ,num_max, math.floor(total_num_in_list / len(test_results))])

# print(get_speed_statistic([5,3,6,2,1,4,5]))


# import math


# def get_speed_statistic(test_results: list) -> list:
#     if test_results == []:
#         return [0, 0, 0]
#
#     num_min = test_results[0]
#     num_max = test_results[0]
#     num_average = math.floor(sum(test_results) / len(test_results))
#
#     for num in test_results:
#         if num < num_min:
#             num_min = num
#         else:
#             if num > num_max:
#                 num_max = num
#
#     return ([num_min, num_max, num_average])

import math


def get_speed_statistic(test_results: list):
    if test_results==[]:
        return [0 , 0 , 0]
    min_num = min(test_results)
    max_num = max(test_results)
    average = math.floor(sum(test_results) / len(test_results))

    return [min_num, max_num, average]


print(get_speed_statistic([1, 5, 3, 6, 7, 8]))
