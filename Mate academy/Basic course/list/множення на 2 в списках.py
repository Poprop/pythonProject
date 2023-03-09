def double_power(current_powers: list) -> list:
    for i in range(len(current_powers)):
        current_powers[i] *= 2
    return current_powers



def double_power(current_powers: list) -> list:
    powers = []
    for power in current_powers:
        powers.append(power * 2)
    return powers
