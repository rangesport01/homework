class Car:
    car_count = 0
    def __init__(self, name, run, year, price, ):
        self.name = name
        self.run = run
        self.year = year
        self.price = price
        self.pricelist = [self.price, self.price * 2.5]



        Car.car_count += 1

    def display_counter(self):
      print('Car Counter is : %d ' % Car.car_count)

    def display_country(self):
        print( f'{car_1.name} in Japan. {car_2.name} in USA.')


    def display_run(self):
        print (f'{car_1.name} is {car_1.run}. {car_2.name} is {car_2.run}')


    def display_car(self):
        print('name : {}. run : {}. year : {}. price : {}'. format(self.name, self.run, self.year, self.price))



    def __str__(self):
        return f"{car_1.name == car_2.name, car_1.year == car_2.year}"


    def __eq__(self, other):
        if isinstance(other, Car):
            return (self.name == other.name)
            return (self.year == other.year)
        return False


car_1 = Car("Mazda", 10000, 1990, 6000)
car_2 = Car ("Dodge", 15000, 2000, 4000)
print(car_1 == car_2)
print(car_1.pricelist)
print(car_2.pricelist)
car_1.display_car()
car_2.display_car()
car_1.display_country()
car_2.display_country()
car_1.display_run()
car_2.display_run()
print('Car Counter is : %d ' % Car.car_count)


"""class Mazeratti(Car):
    def display_country(self):
        print( f'{car_1.name} in Japan. {car_2.name} in USA.')

    def display_country_M(self):
        print (f'Mazeratti is from Italy ')"""


































