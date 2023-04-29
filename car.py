import pygame
import math
from utils import *
from controls import *
from sensors import *

class Car:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.speed = 0
        self.maxSpeed = 5
        self.friction = 0.05
        self.acceleration = 0.3
        self.angle = 0
        self.damaged = False

        self.sensor = Sensor(self)

        self.controls = Controls()
        self.carImage = pygame.transform.scale(pygame.image.load("car2.png").convert_alpha(), (self.width,self.height))
    

    def update(self, roadBorders):
        if not self.damaged:
            self.move()
            self.polygon = self.createPolygon()
            self.damaged = self.assessDamage(roadBorders)
        self.sensor.update(roadBorders)


    def assessDamage(self, roadBorders):
        for i in range(len(roadBorders)):
            if(polysIntersect(self.polygon, roadBorders[i])):
                return True
        return False
    

    def createPolygon(self):
        points = []
        rad = math.hypot(self.width, self.height)/2
        alpha = math.atan2(self.width, self.height)
        points.append([self.x - math.sin(self.angle-alpha)*rad + self.width/2,         translateY(self.y) - math.cos(self.angle-alpha)*rad + self.height/2])
        points.append([self.x - math.sin(self.angle+alpha)*rad + self.width/2,         translateY(self.y) - math.cos(self.angle+alpha)*rad + self.height/2])
        points.append([self.x - math.sin(math.pi+self.angle-alpha)*rad + self.width/2, translateY(self.y) - math.cos(math.pi+self.angle-alpha)*rad + self.height/2])
        points.append([self.x - math.sin(math.pi+self.angle+alpha)*rad + self.width/2, translateY(self.y) - math.cos(math.pi+self.angle+alpha)*rad + self.height/2])
        return points


    def move(self):
        self.controls.listenToKeyboard()

        # Forward Acceleration
        if(self.controls.forward):
            self.speed += self.acceleration

        # Reverse Acceleration
        if self.controls.reverse:
            self.speed -= self.acceleration
        
        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed

        if self.speed < -self.maxSpeed/2:
            self.speed = -self.maxSpeed/2

        if self.speed > 0:
            self.speed -= self.friction
        
        if self.speed < 0:
            self.speed += self.friction

        if abs(self.speed) < self.friction:
            self.speed = 0

        flip = 0
        if self.speed != 0:
            if self.speed > 0:
                flip = 1
            else:
                flip = -1

        # Right and Left Steering. When the speed is either greater or lower than 0, the Steering works.
        if self.controls.right:
            self.angle -= 0.033 * flip
    
        if self.controls.left:
            self.angle += 0.033 * flip

        #print("Speed: ", self.speed, "Angle: ", self.angle)

        self.x -= math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

        self.controls.resetKeys()


    # function to draw the car on the screen
    def draw(self, screen):
        
        self.sensor.draw(screen)
        
        temp_rotated_image = pygame.transform.rotate(self.carImage, math.degrees(self.angle))
        carImage_rect = self.carImage.get_rect(center = (self.width/2 + self.x, self.height/2 + translateY(self.y)))
        rotated_rect = temp_rotated_image.get_rect(center = carImage_rect.center)
        screen.blit(temp_rotated_image, rotated_rect)

        # for i in range(len(self.polygon)):
        #     pygame.draw.line(screen, (0, 0, 0), (self.polygon[i][0], self.polygon[i][1]), (self.polygon[(i+1)%len(self.polygon)][0], self.polygon[(i+1)%len(self.polygon)][1]), 10)
                
        # if not self.damaged:
        #     print("Alive")
        # else:
        #     print("Dead")