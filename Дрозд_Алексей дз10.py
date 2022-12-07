from random import randint

class User:
    def __init__(self, name, surname, birth_year, profession):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.profession = profession
        self.email = name + "@" + surname + ".com"

    def __str__(self):
        return f"{self.email} - {self.birth_year} - {self.profession}"

    def __repr__(self):
        return f"{self.email} - {self.birth_yaer} - {self.profession}"


NAME = ["support", "sales", "info"]
SURNAME = ["asshole", "maggot", "cunt" ]
PROFESSION = ['teacher', 'doctor', 'policeman']

SURNAME_COUNT = len(SURNAME)
NAMES_COUNT = len(NAME)
PROF_COUNT = len(PROFESSION)

def generate_example_1(name, surname, birth_year, profession):
    user_1 = User(name,surname, birth_year,
                profession )
    return user_1


def generate_example_2(name, surname, birth_year, profession):
    user_2 = User(name, surname, birth_year ,
                profession  )
    return user_2
def generate_example_3(name, surname, birth_year, profession):
    user_3 = User(name,surname, birth_year,
                profession )
    return user_3
print(generate_example_3(NAME[randint(0, len(NAME) - 1)], SURNAME[randint(0, len(SURNAME) - 1)],  randint(1990, 2004), "policeman"))
print(generate_example_2(NAME[randint(0, len(NAME) - 1)],SURNAME[randint(0, len(SURNAME) - 1)] ,  randint(1990, 2004), "teacher"))
print(generate_example_1(NAME[randint(0, len(NAME) - 1)], SURNAME[randint(0, len(SURNAME) - 1)],  randint(1990, 2004), "doctor"))