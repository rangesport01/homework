

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.year = year
        self.type = type

    def starting(self):

        return 'автомобиль заведен'


    def ending(self):

        return 'автомобиль заглушен'


    def __str__(self):
     return f"car_1: {self.color}, {self.year}, {self.type}"

car_1 = Car(color="red", type="oil", year=2000)


print(car_1.__str__())
print(Car.starting(car_1))
print(Car.ending(car_1))