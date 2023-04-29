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
road = Road(100, 200 * 0.9)
car = Car(road.getLaneCenter(2),100,30,50, "AI")

traffic = [
    Car(road.getLaneCenter(1), -100, 30, 50, "DUMMY", 2)
]


# main game loop
while not done:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # draw game objects
    screen.fill((211, 211, 211))

    for i in range(len(traffic)):
        traffic[i].update(road.borders, [])

    road.draw(screen)
    for i in range(len(traffic)):
        traffic[i].draw(screen)
    car.update(road.borders, traffic)
    car.draw(screen)

    # Camera tracks the car
    translate(int(-car.y))

    # update screen
    pygame.display.flip()

    # limit FPS
    clock.tick(60)

# quit Pygame
pygame.quit()