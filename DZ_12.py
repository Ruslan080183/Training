import datetime
from random import randint
from DZ_12annotations import UserAnnotation

class User:
    def __init__(self, name, surname, age, country, gender, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.gender = gender
        self.profession = profession
    def __str__(self):
        return F"{self.name} {self.surname} age {self.age} years country {self.country} gender {self.gender} profession {self.profession}"

    def birth_year(self) -> int:
        this_year = int(str(datetime.datetime.now())[0:4])
        birth_year_user = this_year - self.age
        return birth_year_user

    def email(self) -> str:
        email_user = F"{self.name[randint(0,len(self.name) -1)] + self.name[randint(0,len(self.name) -1)]}{self.surname[randint(0,len(self.surname)-1)] + self.surname[randint(0,len(self.surname)-1)]}{User.birth_year(self)}@.com"
        email_user1 = email_user.lower()
        return email_user1

    def user_doctor() -> UserAnnotation:
       doctor = User(name=input("Enter name:"),surname=input("Enter surname:"),age=input("Enter age:"),country=input("Enter country:"),gender=input("Enter gender:"),profession="doctor")
       return doctor

    def user_policeman() -> UserAnnotation:
       policeman = User(name=input("Enter name:"),surname=input("Enter surname:"),age=input("Enter age:"),country=input("Enter country:"),gender=input("Enter gender:"),profession="policeman")
       return policeman

    def user_teacher() -> UserAnnotation:
       teacher = User(name=input("Enter name:"),surname=input("Enter surname:"),age=input("Enter age:"),country=input("Enter country:"),gender=input("Enter gender:"),profession="teacher")
       return teacher





