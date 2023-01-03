


class Cat:
    counter = 0
    def __init__(self, name):
        self.name = name


    def to_answer(self):
        global counter
        Cat.counter += 1
        if Cat.counter % 2 == 0:
            return "meow"
        else:
            return "moor "

cat = Cat("Barsik")
print(cat.to_answer())
print(cat.to_answer())
print(cat.to_answer())
print(cat.to_answer())









"""cat.to_answer()  #-> moor
cat.to_answer()  #-> meow
cat.to_answer()  # -> moor
"""
