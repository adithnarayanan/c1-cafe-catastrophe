import pygame

import pygame_gui 

pygame.init()

# Vars
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 198, 153)
TABLE_COLOR = (140, 77, 10)
ALERT_COLOR = (224, 224, 224)

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

inventory = ['coffee', 'milk', 'sugar']
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

    drawInventory(inventory)
    drawTables()
    drawAlert()
    player()



    pygame.display.update()



pygame.quit()