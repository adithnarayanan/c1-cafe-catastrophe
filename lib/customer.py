import enums
import random

class Customer:
    def __init__(self):
        order = random_coffee()
        max_wait_time = 10

    def random_coffee(self):
        coffee_int = random.randint(1,4)
        if coffee_int == 1:
            return enums.BLACK_COFFEE
        elif coffee_int == 2:
            return enums.MILK_COFFEE
        elif coffee_int == 3:
            return enums.SWEET_BLACK_COFFEE
        else:
            return enums.SWEET_MILK_COFFEE
