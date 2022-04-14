class Animal:
    """Animal class"""
    def __init__(self, genus, species):
        self.__genus = genus
        self.__species = species

    def move(self):
        print(f'{self.__species} is moving')
    
    def sleep(self):
        print(f'{self.__species} is sleeping')

    def eat(self):
        print(f'{self.__species} is eating')

class Book:
    """Book"""
    def __init__(self, title, author, publisher, illustrator, ISBN):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__illustrator = illustrator
        self.__ISBN = ISBN

class Vehicle:
    """Vehicle"""
    def __init__(self, make, model, year, color):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color

    def drive(self):
        print(f'{self.__model} is driving')

    def idle(self):
        print(f'{self.__model} is idling')

    def brake(self):
        print(f'{self.__model} is braking')


