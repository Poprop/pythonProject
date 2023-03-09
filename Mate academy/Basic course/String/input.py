model="Apple iphone 14"


def find_model(search_text: str)->None:
    is_found= search_text.lower() in model.lower()

    if is_found:
        print("Found!")
    else:
        print("Not found")
while True:
    search = input("Enter search text:")
    find_model(search)