from lib.enums import CoffeeTypes
import random
from pygame.image import load
import pygame

class Customer:
    IMAGE_DIM = 64
    img = load('sprites/boy_down.png')
    pygame.font.init()
    customer_font = pygame.font.SysFont('Comic Sans MS', 16)
    BG_COLOR= (255, 255, 255)
    BORDER_COLOR  = (0, 0, 0)
    def __init__(self):
        self.order = self.random_coffee()
        self.max_wait_time = 17

    def random_coffee(self):
        coffee_int = random.randint(1,4)
        if coffee_int == 1:
            return CoffeeTypes.BLACK_COFFEE
        elif coffee_int == 2:
            return CoffeeTypes.MILK_COFFEE
        elif coffee_int == 3:
            return CoffeeTypes.SWEET_BLACK_COFFEE
        else:
            return CoffeeTypes.SWEET_MILK_COFFEE

    def draw(self, screen, x, y):
        screen.blit(self.img, (x-self.IMAGE_DIM/2, y))
        img_offset = 4
       # pygame.draw.rect(screen, self.BORDER_COLOR, pygame.Rect(x-50 - self.IMAGE_DIM/2, y-100, 100, 100))
        #pygame.draw.rect(screen, self.BG_COLOR, pygame.Rect(x-50 - self.IMAGE_DIM/2 + img_offset, y-100 + img_offset, 80, 80))
        string = self.order.value
        parts = string.split(" ")
        x_coord = x - self.IMAGE_DIM/2 + 5
        y_coord = y - 60
        for part in parts:
            text_surface = self.customer_font.render(part, False, (0, 0, 0))
            screen.blit(text_surface, (x_coord, y_coord))
            y_coord = y_coord + 18
        