country = {"code": 'UA', 'Name':"Ukrainian" , 'population': 45,  }
#print(country["code"])
#print(country.get("code")) #добування інформації поключу без []

#country.clear()
#print(country)

#country.pop('Name') #видалення якогось елементу за ключем із словника
#print(country)

#country.popitem() #функція видалення останнього елементу
#print(country)

#print(country.keys())   #ключі
#print(country.values()) #значення
#print(country.items()) # все в словнику

country['code'] = 'None'
print(country.items())