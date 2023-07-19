import pygame

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


playerImg = pygame.image.load('src/assets/waiter.png')
playerX = 500 - playerImg.get_width()/2
playerY = 400 - playerImg.get_height()/2
def player():
    screen.blit(playerImg, (playerX, playerY))

def drawTables():
    #(250, 250)
    pygame.draw.rect(screen, TABLE_COLOR, pygame.Rect(250 , 250, 500, 100))

    #(250, 450)
    pygame.draw.rect(screen, TABLE_COLOR, pygame.Rect(250 , 450, 500, 100))

run = True


while run:

    #draw screen
    screen.fill((BACKGROUND_COLOR))

    #draw two tables
    
    
    #draw player

    #draw coffee machine

    #draw cutsomers

    #player movement
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drawTables()
    player()
    pygame.display.update()

pygame.quit()