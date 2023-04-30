import pygame
from car import *
from road import *
from visualizer import *

# initialize Pygame
pygame.init()

# set up screen
size = (600, 400)
screen = pygame.display.set_mode(size, pygame.SRCALPHA)
pygame.display.set_caption("Neural Network")

# set up game loop
done = False
clock = pygame.time.Clock()

# Create the car and other elements
road = Road(100, 200 * 0.9)
car = Car(road.getLaneCenter(2),100,30,50, "KEYS")

# All the cars in the traffic will be in this array
traffic = [
    Car(road.getLaneCenter(1), -100, 30, 50, "DUMMY", 2),
    Car(road.getLaneCenter(0), -200, 30, 50, "DUMMY", 2),
    Car(road.getLaneCenter(2), -300, 30, 50, "DUMMY", 2),
    Car(road.getLaneCenter(1), -400, 30, 50, "DUMMY", 2),
    Car(road.getLaneCenter(0), -600, 30, 50, "DUMMY", 2)
]


# main game loop
while not done:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # draw game objects
    screen.fill((211, 211, 211))

    # Check borders for all cars in traffic
    for i in range(len(traffic)):
        traffic[i].update(road.borders, [])

    # Draw the road on the screen
    road.draw(screen)

    # Draw all the cars in the traffic
    for i in range(len(traffic)):
        traffic[i].draw(screen)
    
    # Check collisions with borders
    car.update(road.borders, traffic)
    # Draw the car on the screen
    car.draw(screen)
    
    # Camera tracks the car
    translate(int(-car.y))

    # Visualisation Of Network
    Visualizer.drawNetwork(screen, car.brain)
    
    # update screen
    pygame.display.flip()

    # limit FPS
    clock.tick(60)

# quit Pygame
pygame.quit()