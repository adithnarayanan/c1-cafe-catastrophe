import pygame

from src.player import Player
from lib.coffee_machine import CoffeeMachine
from lib.enums import Directions, Ingredients, CoffeeTypes

pygame.init()

# Vars
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 198, 153)
TABLE_COLOR = (140, 77, 10)
ALERT_COLOR = (224, 224, 224)
IMAGE_DIM = 64
ALERT_COLOR = (244, 244, 244)
INVENTORY_BG_COLOR = (255, 255, 255)
INVENTORY_BORDER_COLOR = (255, 102, 102)
# Font stuff
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 10)

# Main screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#title and icon
pygame.display.set_caption("C1 Cafe Catastrope")
icon = pygame.image.load('src/assets/CapOneLogo.png')
pygame.display.set_icon(icon)


#playerInfo:
coffeeBeansImg = pygame.image.load('src/assets/coffee-beans.png')
milkImg = pygame.image.load('src/assets/milk.png')
sugarImg = pygame.image.load('src/assets/sugar.png')
coffeeMachineImg = pygame.image.load('src/assets/coffee-machine.png')
ingredients_dict = {'COFFEE_BEANS': coffeeBeansImg, 'SUGAR': sugarImg, 'MILK': milkImg}
bottomTableImages = [coffeeMachineImg, coffeeBeansImg, milkImg, sugarImg]

# objects
player = Player(SCREEN_WIDTH/2, 400, 250, 750)
coffeeMachine = CoffeeMachine()

interactionPointsX = [312.5, 437.5, 562.5, 687.5]

locationsToIngredientsDict = {1: Ingredients.COFFEE_BEANS, 2: Ingredients.MILK, 3: Ingredients.SUGAR}

def drawTables():
    #(250, 250)
    pygame.draw.rect(screen, TABLE_COLOR, pygame.Rect(250 , 250, 500, 100), 0 , 20)

    #(250, 450)
    pygame.draw.rect(screen, TABLE_COLOR, pygame.Rect(250 , 450, 500, 100), 0, 20)
    bottomTableY = 500 - IMAGE_DIM/2

    curr_width = 250 + 125/2 - 32
    for img in bottomTableImages:
        screen.blit(img, (curr_width, bottomTableY))
        curr_width += 125

def interact():
    print("checking for collisions")
    
    print(player.currDirection)
    if (player.currDirection == Directions.DOWN):
        #print("here")
        for i in range(4):
            print(abs(player.x - interactionPointsX[i]))
            if (abs(player.x - interactionPointsX[i]) <= 50):
                #print("here")
                if (i == 0):
                    #coffee machine interaction
                    coffee_or_none = coffeeMachine.add_ingredient(player.inventory[0])
                    if coffee_or_none in CoffeeTypes:
                        print("******")
                        player.inventory[0] = coffee_or_none
                    elif coffee_or_none in Ingredients:
                        player.inventory.clear()
                    
                else:
                    player.tryToAdd(locationsToIngredientsDict[i])
    
    if (player.currDirection == Directions.UP):
        #handle customer interactions
        return None

images_dict = {}
inventory = ['coffee', 'milk', 'sugar']
def drawInventory(user_items):
    inv_x, inv_y = 15, 15
    img_offset = 10

    def showItemInInventory(image, x, y, item):
        screen.blit(image, (x, y))

    num_items = len(user_items)
    pygame.draw.rect(screen, INVENTORY_BORDER_COLOR, pygame.Rect(inv_x, inv_y, 100, 100))
    pygame.draw.rect(screen, INVENTORY_BG_COLOR, pygame.Rect(inv_x + img_offset, inv_y + img_offset, 80, 80))
    if len(user_items) > 0:
        item = user_items[0].name
        item_img = ingredients_dict[item]
        coords = item_img.get_rect().center
        print(coords)
        showItemInInventory(ingredients_dict[item], inv_x + abs(50 - coords[0]), inv_y + abs(50 - coords[1]), item)


def drawAlert():
    pygame.draw.rect(screen, ALERT_COLOR, pygame.Rect(SCREEN_WIDTH//2 - 0.125*SCREEN_WIDTH, SCREEN_HEIGHT//2 - 0.125*SCREEN_HEIGHT, 0.25*SCREEN_WIDTH, 0.25*SCREEN_HEIGHT))

run = True

clock = pygame.time.Clock()

while run:

    #draw screen
    screen.fill((BACKGROUND_COLOR))


    #draw two tables
    
    #draw player

    #draw coffee machine

    #draw cutsomers

    #player movement

    key = pygame.key.get_pressed()

    player.handleMovement(key)

    player.clearInventory(key)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                interact()
            #player.tryToAdd()
    drawInventory(inventory)
    drawTables()
    drawInventory(player.inventory)
    player.draw(screen)
    pygame.display.update()
    clock.tick(30)



pygame.quit()