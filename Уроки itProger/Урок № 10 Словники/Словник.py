#contry = {4: 3 } #перше значення ключ , друге - інформація що видається при введенні ключа
#print(country[4])

country = {"code": 'UA', 'Name':"Ukrainian" , 'population': 45,  }
#country = dict (code='UA', Name="Ukraine") інший спосіб запису словників
#print(country['Name'])
#print(country)

#for key in  country:
    #print(key)     в такому випадку виводяться лише ключы

for key, value in country.items():
    print(key, "-", value)   # в такому випадку і ключі і значення

