file = open('Data/text.txt', "a")   # 'w' - формат щоб відкривати файл кожен раз по новій
file.write('Hello')     # 'a' формат додає в старий файл нові данні
file.write('!!!')
file.close()