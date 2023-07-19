from enum import Enum

class Ingredient(Enum):
    COFFEE_BEANS = 1
    MILK = 2
    SUGAR = 3

class CoffeeTypes(Enum):
    BLACK_COFFEE = 1
    MILK_COFFEE = 2
    SWEET_COFFEE = 3
    SWEET_MILK_COFFEE = 4

class Direction(Enum) :
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4