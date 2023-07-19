import pygame

from src.player import Player

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 198, 153)
TABLE_COLOR = (140, 77, 10)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#title and icon
pygame.display.set_caption("C1 Cafe Catastrope")
icon = pygame.image.load('src/assets/CapOneLogo.png')
pygame.display.set_icon(icon)


#playerInfo:
playerImg = pygame.image.load('sprites/boy_down.png')
coffeeBeansImg = pygame.image.load('src/assets/coffee-beans.png')
milkImg = pygame.image.load('src/assets/milk.png')
sugarImg = pygame.image.load('src/assets/sugar.png')
coffeeMachineImg = pygame.image.load('src/assets/coffee-machine.png')

bottomTableImages = [coffeeMachineImg, coffeeBeansImg, milkImg, sugarImg]

player = Player(500 - 32, 400 - 32, 250, 750)
# playerX = 500 - playerImg.get_width()/2
# playerY = 400 - playerImg.get_height()/2

# def player():
#     screen.blit(playerImg, (playerX, playerY))

def drawTables():
    #(250, 250)
    pygame.draw.rect(screen, TABLE_COLOR, pygame.Rect(250 , 250, 500, 100), 0 , 20)

    #(250, 450)
    pygame.draw.rect(screen, TABLE_COLOR, pygame.Rect(250 , 450, 500, 100), 0, 20)
    bottomTableY = 500-32
    curr_width = 250 + 125/2 - 32
    for img in bottomTableImages:
        screen.blit(img, (curr_width, bottomTableY))
        curr_width += 125

# def displayInventory():
#     asdf

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
    # if (key[pygame.K_a] and playerX > 250):
    #     playerX = playerX - 5
    #    # print("working")
    # if (key[pygame.K_d] and playerX < 750 - playerImg.get_width()):
    #     playerX = playerX + 5
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drawTables()
    player.draw(screen)
    pygame.display.update()
    clock.tick(30)

pygame.quit()