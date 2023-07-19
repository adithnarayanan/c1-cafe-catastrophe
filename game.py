import pygame

from src.player import Player
from lib.enums import Directions, Ingredients

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 198, 153)
TABLE_COLOR = (140, 77, 10)
IMAGE_DIM = 64

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

bottomTableImages = [coffeeMachineImg, coffeeBeansImg, milkImg, sugarImg]

player = Player(SCREEN_WIDTH/2, 400, 250, 750)

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

def checkForCollisions():
    print("checking for collisions")
    
    print(player.currDirection)
    if (player.currDirection == Directions.DOWN):
        print("here")
        for i in range(4):
            print(abs(player.x - interactionPointsX[i]))
            if (abs(player.x - interactionPointsX[i]) <= 50):
                print("here")
                if (i == 0):
                    #coffee machine interaction
                    return None
                else:
                    player.tryToAdd(locationsToIngredientsDict[i])
    
    if (player.currDirection == Directions.UP):
        #handle customer interactions
        return None

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
                checkForCollisions()
            #player.tryToAdd()

    drawTables()
    player.draw(screen)
    pygame.display.update()
    clock.tick(30)

pygame.quit()