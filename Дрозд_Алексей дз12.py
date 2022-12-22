import math


class Snow:
    def __init__(self, quantity_of_snowflakes):
        self.quantity_of_snowflakes = int(quantity_of_snowflakes)


    def __add__(self, n):
        return self.quantity_of_snowflakes + n

    def __sub__(self, n):
        return self.quantity_of_snowflakes - n

    def __mul__(self, n):
        return self.quantity_of_snowflakes * n

    def __truediv__(self, n):
        return self.quantity_of_snowflakes // n

    def __call__(self, new_quantity):
        self.quantity_of_snowflakes = new_quantity

    def makeSnow(self, quantity_of_snowflakes_in_a_row):
        string_of_snowflakes = ""
        quantity_of_row = int(self.quantity_of_snowflakes) // quantity_of_snowflakes_in_a_row
        for i in range(quantity_of_row):
            string_of_snowflakes += ("*" * quantity_of_snowflakes_in_a_row)
            string_of_snowflakes += "\n"
        rest_of_snowflakes = (int(self.quantity_of_snowflakes) - quantity_of_row * quantity_of_snowflakes_in_a_row)
        string_of_snowflakes += "*" * rest_of_snowflakes
        return string_of_snowflakes

snowflakes = Snow('100')
quantity_of_snowflakes_in_a_row = 10
print(snowflakes.makeSnow(quantity_of_snowflakes_in_a_row))