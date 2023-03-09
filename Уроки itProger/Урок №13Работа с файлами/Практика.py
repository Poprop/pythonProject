data= input ('Введите текст:')

file = open('Data/text.txt', "a")   # 'w' - формат щоб відкривати файл кожен раз по новій
file.write(data + '\n')     # 'a' формат додає в старий файл нові данні

file.close()