import pygame
import math
from controls import *

class Car:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.speed = 0
        self.maxSpeed = 3
        self.friction = 0.05
        self.acceleration = 0.2
        self.angle = 0

        self.controls = Controls()
        # self.carImage = pygame.image.load("car2.png").convert_alpha()
        self.carImage = pygame.transform.scale(pygame.image.load("car2.png").convert_alpha(), (self.width,self.height))
    

    def update(self):
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

        # Right and Left Steering. When the speed is either greater or lower than 0, the Steering works.
        if self.controls.right and (self.speed>0 or self.speed<0):
            self.angle -= 0.033
    
        if self.controls.left and (self.speed>0 or self.speed<0):
            self.angle += 0.033

        #print("Speed: ", self.speed, "Angle: ", self.angle)

        self.x -= math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

        self.controls.resetKeys()
        

    # function to draw the car on the screen
    def draw(self, screen):
        
        temp_rotated_image = pygame.transform.rotate(self.carImage, math.degrees(self.angle))
        center = temp_rotated_image.get_rect().center
        screen.blit(temp_rotated_image, (self.x- self.width/2 , self.y - self.height/2))

        # self.angle += 0.01               # This is the the code I wrote to just debug. It should not be here!!
        # screen.blit(pygame.transform.rotate(self.carImage, math.degrees(self.angle)), self.carImage.get_rect(center = (self.x -self.width/2, self.y - self.height/2)))
        # pygame.draw.rect(screen, (0,0,0), pygame.Rect(
        #     self.x - self.width/2,
        #     self.y - self.height/2,
        #     self.width,
        #     self.height))
