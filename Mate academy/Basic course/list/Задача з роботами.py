# def get_plan(current_production: int, month: int, percent: int) -> list:
#      profit = current_production
#      for number_monthes in range(month):
#          profit *= 1 + percent / 100
#      return round([profit - current_production])


# def get_plan(current_production: int, month: int, percent: int):


# def calculate_profit( amount: int, percent: Union[float, int], period: int) -> int:
#     profit = amount
#     for year in range(period):
#         profit *= 1 + percent / 100
#     return profit - amount

import math
def get_plan(current_production: int, month: int, percent: int):
    array = []
    current = current_production
    for i in range(month):
        i += 1
        current = math.floor(current * (100 + percent) / 100)
        array.append(current)
    return array
x=get_plan(1000 , 4 , 10)
print(x)