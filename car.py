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
        self.carImage = pygame.transform.scale(pygame.image.load("car2.png").convert_alpha(), (self.width,self.height))
    

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

    def update(self):
        self.move()

    # function to draw the car on the screen
    def draw(self, screen):
        
        temp_rotated_image = pygame.transform.rotate(self.carImage, math.degrees(self.angle))
        carImage_rect = self.carImage.get_rect(center = (self.width/2 + self.x, self.height/2 +self.y))
        rotated_rect = temp_rotated_image.get_rect(center = carImage_rect.center)
        screen.blit(temp_rotated_image, rotated_rect)

