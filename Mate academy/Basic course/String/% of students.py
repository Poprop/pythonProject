# list = "1010101111"
# number_of_characters = len(list)
# x=list.count("1")
# print(x)
# percent = int((x / number_of_characters) * 100)
# print(percent)
#


def get_success_rate(statistics: str) -> int:
    if statistics == "":
        return 0

    number_of_characters = len(statistics)
    x = statistics.count("1")
    percent = int((x / number_of_characters) * 100)
    return round(percent)


result = get_success_rate("11100")
print(result)
