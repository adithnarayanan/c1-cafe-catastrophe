import pygame

from src.player import Player
from lib.enums import Directions, Ingredients

pygame.init()

# Vars
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 198, 153)
TABLE_COLOR = (140, 77, 10)
IMAGE_DIM = 64

# Font stuff
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)

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

images_dict = {}
def drawInventory(user_items):
    inv_x, inv_y = 0, 0
    desc_offset = 75
    img_offset = 25

    def showItemInInventory(image, x, y, item):
        screen.blit(image, (x, y))
        text_surface = my_font.render(f'{item}', False, (0, 0, 0))
        screen.blit(text_surface, (x, y+desc_offset))

    num_items = len(user_items)
    pygame.draw.rect(screen, TABLE_COLOR, pygame.Rect(inv_x, inv_y, num_items * 100, 100))
    
    showItemInInventory(playerImg, inv_x + img_offset, inv_y + img_offset, user_items[0])


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
                checkForCollisions()
            #player.tryToAdd()

    drawTables()
    player.draw(screen)
    pygame.display.update()
    clock.tick(30)



pygame.quit()