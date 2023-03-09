# def is_werewolf(target):
#    return target.lower() == target.translate(str.maketrans('','','.,:;-?! ')).lower()[::-1]

# result1 = is_werewolf("rotator,Rotator rOtator")
# print(result1)

def is_werewolf(target: str) -> bool:

   target = target.lower().replace(" ", '').replace(',', '').replace('.', '').replace('!', '').replace('?',
                                                                                                       '').replace(';',
                                                                                                                        '')

    return target == target[::-1]


result1 = is_werewolf("vrotator ")
print(result1)


def is_werewolf(target: str) -> bool:
    ignored_symbols = " .,:;!?\"'(){}<>"
    prepared_target = ""
    for letter in target:
        if letter not in ignored_symbols:
            prepared_target += letter
    prepared_target = prepared_target.upper()
    return prepared_target[::-1] == prepared_target