
from pygame import K_a, K_d, K_w, K_s, K_e
from pygame.image import load
from lib.enums import Directions, Ingredients
#import pygame

class Player:
    PLAYER_MOVEMENT_SPEED = 5
    IMAGE_DIM = 64
    
    lookingUpImg = load('sprites/boy_up.png')
    lookingDownImg = load('sprites/boy_down.png')
    lookingLeftImg = load('sprites/boy_left.png')
    lookingRightImg = load('sprites/boy_right.png')


    imgDict = {Directions.UP: lookingUpImg, Directions.DOWN: lookingDownImg, Directions.LEFT: lookingLeftImg, Directions.RIGHT: lookingRightImg}

    currDirection = Directions.LEFT

    inventory = []

    #Note x and y refer to the middle of the player
    def __init__(self, xstart, ystart, leftBound, rightBound) -> None:
        self.x = xstart
        self.y = ystart
        self.leftBound = leftBound
        self.rightBound = rightBound
        

    def handleMovement(self, key):
        if (key[K_a] == 1):
            self.currDirection = Directions.LEFT
            if (self.x > self.leftBound):
                self.x = self.x - self.PLAYER_MOVEMENT_SPEED
        if (key[K_d]):
            self.currDirection = Directions.RIGHT
            if (self.x < self.rightBound - self.IMAGE_DIM):
                self.x = self.x + self.PLAYER_MOVEMENT_SPEED

        if (key[K_w]):
            self.currDirection = Directions.UP

        if (key[K_s]):
            self.currDirection = Directions.DOWN

    def clearInventory(self, key):
        if (key[K_e]):
            self.inventory.clear()

    def tryToAdd(self, ingredient):
        if (len(self.inventory) > 0):
            #already have something in inventory
            return None
        else:
            self.inventory.append(ingredient)

    def draw(self, screen):
        screen.blit(self.imgDict[self.currDirection], (self.x - self.IMAGE_DIM/2, self.y - self.IMAGE_DIM/2))
        print(self.inventory)