#методи введенння кортежів - зі () або без них але з додаванням ,
#data = 5 , 6 , True
#data = (5,)
#data = (5 , 6 , True)
#print(data)

data = (5 , 6 , 4 , 3 , 5.4 , 'hello', True)
for el in data:
    print(el)

nums = [5 , 7 , 2]
new_data = tuple(nums)ж
print(new_data)
#new_data = tuple(nums)
#word = tuple('hello world')
#new_word = tuple(word)
#print(new_data)
#print(word)