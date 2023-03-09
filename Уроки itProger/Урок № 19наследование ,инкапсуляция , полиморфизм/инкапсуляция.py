

class Building:
   __year = None
   __city = None  #інкапсуляція це за допомогою __ заборона прямого звернення до змінних


    def __init__(self, year , city ):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year", self.year , ". City:" , self.city)

class School (Building):
    pupils = 0
    def __init__(self , pupils, year , city):
        super(School , self).__init__(year , city)
        self.pupils = pupils
    def get_info(self):
        super().get_info()
        print("Pupils", self.pupils)
class House (Building):
    pass

class Shop ( Building):
    pass


school = School (100 ,  2000 , 'Kiyew')
school.get_info()
house = House (2010 , ' Cherkassy')
shop = Shop ( 2009 , 'Kharkow')

shop.get_info()
