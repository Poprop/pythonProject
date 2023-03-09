def make_abbr(words):
    abbr=""
    for word in words.split(""):
       abbr=abbr+word[0].upper()
    return abbr
func=make_abbr("Ебать хуйня питон")
print(func)
