import enums

class CoffeeMachine:
    def __init__(self):
        self.inventory = []

        #amount of time for coffee to brew, ignore for now
        self.brew_time = 5
        self.in_use = False
    
    
    def add_ingredient(self, ingredient):
        make_coffee = False

        #check if ingredient is already in inventory
        if ingredient in self.inventory:
            #alert: You already added this ingredient!
            return None

        #if you are adding the last ingredient, either make coffee or alert that they didnt add coffee beans to the machine
        if len(inventory) == 2:
            if Ingredients.COFFEE_BEANS in self.inventory:
                    inventory.append(ingredient)
                    return brew_coffee()
            else:
                if ingredient == Ingredients.COFFEE_BEANS:
                    inventory.append(ingredient)
                    return brew_coffee()
                else:
                    #alert: You need to add Coffee beans to make Coffee!
                    return None
        #if you are not adding the last ingredient, add the ingredient and check if the player wants to make coffee now or add more ingredients
        else:
            inventory.append(ingredient)
            #alert: Do you want to make coffee now? If yes, make_coffee = True

            if make_coffee:
                return brew_coffee()

    def brew_coffee(self):
        coffee = CoffeeTypes.BLACK_COFFEE

        if Ingredients.MILK in self.inventory and Ingredients.SUGAR in self.inventory:
            coffee = CoffeeTypes.SWEET_MILK_COFFEE
        elif not Ingredients.MILK in self.inventory:
            coffee = CoffeeTypes.SWEET_BLACK_COFFEE
        elif not Ingredients.SUGAR in self.inventory:
            coffee = CoffeeTypes.MILK_COFFEE

        clear_inv()
        return coffee

    def clear_inv(self):
        inventory.clear()
