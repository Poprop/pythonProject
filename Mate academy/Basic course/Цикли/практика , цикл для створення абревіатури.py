def make_abbr(words):
    abbr = ""
    for word in words.split( ):
        abbr += word[0].upper()
    return (abbr)


result = make_abbr("Да  ебать  втянули меня в эту...")
print(result)
