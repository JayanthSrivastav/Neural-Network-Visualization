import pygame
from car import *
from road import *
from visualizer import *
import os
import json
import threading

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

# Function to save weights.
def save():
    with open('weight.json', 'w') as w:
        save_dic = {'levels': ([vars(bestCar.brain.levels[0]), vars(bestCar.brain.levels[1])])}
        #w.write(str(save_dic))
        #w.close()
        js = json.dumps(save_dic)
        w.write(js)
        w.close
        
# Function to generate N cars.
def generateCars(N):
    cars = []
    for i in range(N):
        cars.append(Car(road.getLaneCenter(1),100,30,50, "AI"))
    return cars

N = 100
cars = generateCars(N)
bestCar = cars[0]
if os.path.exists('weight.json'):
    with open('weight.json', 'r') as f:
        data = json.load(f)
        f.close()
    for i in range(len(cars)):
        cars[i].brain.levels[0].inputs = data['levels'][0]['inputs']
        cars[i].brain.levels[0].outputs = data['levels'][0]['outputs']
        cars[i].brain.levels[0].weights = data['levels'][0]['weights']
        cars[i].brain.levels[0].biases = data['levels'][0]['biases']

        cars[i].brain.levels[1].inputs = data['levels'][1]['inputs']
        cars[i].brain.levels[1].outputs = data['levels'][1]['outputs']
        cars[i].brain.levels[1].weights = data['levels'][1]['weights']
        cars[i].brain.levels[1].biases = data['levels'][1]['biases']

        # Genetic Algorithm.
        # Remove this part to see all carsgo in unison following the saved weights.
        if i!=0:
            NeuralNetwork.mutate(cars[i].brain, 0.1)

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save()

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
    
    # Function to find the best car among N cars. Best car is the car which is on the lead.
    # Try to modify this logic if possible, it works greatly but I feel two lists are unnecessary.
    def findBestCar(cars):
        new = []
        new2 = []
        for i in cars:
            new.append(i)
            new2.append(i.y)

        c = new[new2.index(min(new2))]

        return c

    # Best Car.
    bestCar = findBestCar(cars)
    #print(bestCar)

    # To update N cars.
    for i in range(len(cars)):
        cars[i].update(road.borders, traffic)

    # To draw N cars and set their transparency to 50.
    for i in range(len(cars)):
        cars[i].carImage.set_alpha(50)
        cars[i].draw(screen)

    # To draw the best car and set its transparency to 255.
    bestCar.carImage.set_alpha(255)
    bestCar.draw(screen, True)

    # Camera tracks the best car.
    translate(int(-bestCar.y))

    # Visualisation Of Network
    Visualizer.drawNetwork(screen, bestCar.brain)
    
    # update screen
    pygame.display.flip()

    # limit FPS
    clock.tick(60)

# quit Pygame
pygame.quit()
