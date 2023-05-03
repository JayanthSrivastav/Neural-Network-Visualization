import pygame

from utils import *
class Road:
    def __init__(self, x, width, laneCount = 3):
        self.x = x
        self.width = width
        self.laneCount = laneCount

        self.left = int(x - width/2)
        self.right = int(x + width/2)

        infinity = 1000000
        self.top = -infinity
        self.bottom = infinity

        self.dashLength = 20
        self.gapLength = 40
        
        # The Borders for Collision Detection System
        topLeft = [self.left, self.top]
        topRight = [self.right, self.top]
        bottomLeft = [self.left, self.bottom]
        bottomRight = [self.right, self.bottom]

        
        self.borders = [
            [topLeft, bottomLeft],
            [topRight, bottomRight]
        ]


    def getLaneCenter(self, laneIndex):
        laneWidth = self.width/self.laneCount
        return self.left + laneWidth/2 + laneIndex*laneWidth - 15

    def draw(self,screen):
        lineWidth = 5

        for i in range(self.laneCount+1):
            x = lerp(self.left, self.right, i/self.laneCount)
            if i > 0 and i < self.laneCount:
                for j in range(translateY(self.top), translateY(self.bottom), self.dashLength + self.gapLength):
                    pygame.draw.line(screen, (255,255,255), (x+400, j), (x+400, j+self.dashLength), lineWidth)
            else:
                pygame.draw.line(screen, (255,255,255), (x+400, translateY(self.top)), (x+400, translateY(self.bottom)), lineWidth)