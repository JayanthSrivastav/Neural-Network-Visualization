import pygame
from car import *
from road import *

# initialize Pygame
pygame.init()

# set up screen
size = (200, 400)
screen = pygame.display.set_mode(size, pygame.SRCALPHA)
pygame.display.set_caption("Neural Network")

# set up game loop
done = False
clock = pygame.time.Clock()

# Create the car and other elements
car = Car(85,100,35,55)
road = Road(100, 200 * 0.9)


# main game loop
while not done:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # draw game objects
    screen.fill((211, 211, 211))
    road.draw(screen)
    car.draw(screen)
    car.update()

    # Camera tracks the car
    translate(int(-car.y))

    # update screen
    pygame.display.flip()

    # limit FPS
    clock.tick(60)

# quit Pygame
pygame.quit()