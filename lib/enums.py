from enum import Enum

class Ingredients(Enum):
    COFFEE_BEANS = 1
    MILK = 2
    SUGAR = 3

class CoffeeTypes(Enum):
    BLACK_COFFEE = "Black Coffee"
    MILK_COFFEE = "Milk Coffee"
    SWEET_BLACK_COFFEE = "Sweet Black Coffee"
    SWEET_MILK_COFFEE = "Sweet Milk Coffee"

class Directions(Enum) :
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4