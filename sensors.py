import math
import pygame
from utils import *

class Sensor:
    def __init__(self, car):
        self.car = car
        self.rayCount = 5
        self.rayLength = 100
        self.raySpread = 90
        self.rays = []
        self.readings = []

    def update(self, roadBorders, traffic):
        self.castRays()
        self.readings = []
        for i in range(len(self.rays)):
            self.readings.append(self.getReading(self.rays[i], roadBorders, traffic))
    

    def getReading(self, ray, roadBorders, traffic):
        touches = []
        for i in range(len(roadBorders)):
            touch = getIntersection(ray[0], ray[1], roadBorders[i][0], roadBorders[i][1])
            if touch:
                touches.append(touch)
        
        for i in range(len(traffic)):
            poly = traffic[i].polygon
            for j in range(len(poly)):
                value = getIntersection(ray[0], ray[1], poly[j], poly[(j+1)%len(poly)])
                if value:
                    touches.append(value)

        if len(touches) == 0:
            return 0
        else:
            offsets = []
            for t in touches:
                offsets.append(t[2])
            for t in touches:
                if t[2] == min(offsets):
                    return t



    def castRays(self):
        self.rays = []
        for i in range(self.rayCount):
            rayAngle = lerp(self.raySpread/2, -self.raySpread/2, i/(self.rayCount-1)) + math.degrees(self.car.angle)
            start = [self.car.x + self.car.width/2, translateY(self.car.y) + self.car.height/2]
            end = [self.car.x + self.car.width/2 - math.sin(math.radians(rayAngle)) * self.rayLength, translateY(self.car.y) + self.car.height/2 - math.cos(math.radians(rayAngle)) * self.rayLength]
            self.rays.append([start,end])

    
    def draw(self, screen):
        for i in range(self.rayCount):
            end = self.rays[i][1]
            if self.readings[i]:
                end = self.readings[i]
            pygame.draw.line(screen, (0, 0, 0), (end[0], end[1]), (self.rays[i][1][0], self.rays[i][1][1]), 2)
            pygame.draw.line(screen, (230, 185, 90), (self.rays[i][0][0], self.rays[i][0][1]), (end[0], end[1]), 2)