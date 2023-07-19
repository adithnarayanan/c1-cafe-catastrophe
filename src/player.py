
from pygame import K_a, K_d, K_w, K_s
from pygame.image import load
from src.direction import Direction
#import pygame

class Player:
    PLAYER_MOVEMENT_SPEED = 5
    IMAGE_DIM = 64
    
    lookingUpImg = load('sprites/boy_up.png')
    lookingDownImg = load('sprites/boy_down.png')
    lookingLeftImg = load('sprites/boy_left.png')
    lookingRightImg = load('sprites/boy_right.png')


    imgDict = {Direction.UP: lookingUpImg, Direction.DOWN: lookingDownImg, Direction.LEFT: lookingLeftImg, Direction.RIGHT: lookingRightImg}

    currDirection = Direction.LEFT

    def __init__(self, xstart, ystart, leftBound, rightBound) -> None:
        self.x = xstart
        self.y = ystart
        self.leftBound = leftBound
        self.rightBound = rightBound
        

    def handleMovement(self, key):
        if (key[K_a] == 1):
            self.currDirection = Direction.LEFT
            if (self.x > self.leftBound):
                self.x = self.x - self.PLAYER_MOVEMENT_SPEED
        if (key[K_d]):
            self.currDirection = Direction.RIGHT
            if (self.x < self.rightBound - self.IMAGE_DIM):
                self.x = self.x + self.PLAYER_MOVEMENT_SPEED

        if (key[K_w]):
            self.currDirection = Direction.UP

        if (key[K_s]):
            self.currDirection = Direction.DOWN

    def draw(self, screen):
        screen.blit(self.imgDict[self.currDirection], (self.x, self.y))