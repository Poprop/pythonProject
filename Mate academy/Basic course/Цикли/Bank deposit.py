# def calculate_profit(amount: int, percent: [float, int], period: int) -> [float, int]:
#     if amount == 0:
#         return 0
#     if percent == 0:
#         return 0
#     if period == 0:
#         return 0
#
#     Initial_value = amount
#     years = 0
#     while period > years:
#         amount = amount * (1 + percent / 100)
#         years += 1
#     return amount - Initial_value
#
#
# print(calculate_profit(1000, 10, 2))


# def calculate_profit(
#    amount: int, percent:[float, int], period: int
# ) -> int:
#    profit = amount
#    for year in range(period):
#       profit *= 1 + percent / 100
#   return profit - amount
# x=calculate_profit(1000, 10, 2)


def calculate_profit(
        amount: int, percent: [float, int], period: int
) -> int:
    profit = amount
    for year in range(period):
        profit *= 1 + percent / 100
    return round(profit - amount)
