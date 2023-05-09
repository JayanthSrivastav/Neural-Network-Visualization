#import pygame
from car import *
from road import *
from visualizer import *
import pickle
from text import *
import os


showOnlyBestCar = 0
randomInfiniteTraffic = 1
carsPerGeneration = 200
contType = 1

genNumber = 0
alive = carsPerGeneration
showSensors = True

def generateCars(N):
    cars = []
    if contType == 0:
        cars.append( Car(road.getLaneCenter(1),100,30,50,"KEYS"))
    else:
        for i in range(1, N+1):
            cars.append( Car(road.getLaneCenter(1),100,30,50,"AI"))
    return cars

def save():
    global bestCar, genNumber
    with open("bestCar.pickle", "wb") as f:
        pickle.dump(bestCar.brain, f)
    f = open("genDat.txt","w")
    f.write(str(genNumber+1))
    # f.close()

def discard():
    pass

def next_gen():
    global cars, traffic, genNumber
    cars = []
    if showOnlyBestCar:
        cars = generateCars(1)
    else:
        cars = generateCars(carsPerGeneration)
    bestCar = cars[0]
    try:
        with open("bestCar.pickle", "rb") as f:
            bestCar.brain = pickle.load(f)
            f = open("genDat.txt", "r")
            genNumber = int(f.read())
            f.close()
        for i in range(len(cars)):
            for l in range(len(cars[i].brain.levels)):
                cars[i].brain.levels[l].inputs = bestCar.brain.levels[l].inputs.copy()
                cars[i].brain.levels[l].outputs = bestCar.brain.levels[l].outputs.copy()
                cars[i].brain.levels[l].biases = bestCar.brain.levels[l].biases.copy()
                for w in range(len(cars[i].brain.levels[l].weights)):
                    cars[i].brain.levels[l].weights[w] = bestCar.brain.levels[l].weights[w].copy()
            if i != 0:
                NeuralNetwork.mutate(cars[i].brain, 0.1)
        
    except:
        pass

    # All the cars in the traffic will be in this array
    traffic = [
        Car(road.getLaneCenter(1), -100, 30, 50, "DUMMY", 2),
        Car(road.getLaneCenter(0), -200, 30, 50, "DUMMY", 2),
        Car(road.getLaneCenter(2), -300, 30, 50, "DUMMY", 2),
        Car(road.getLaneCenter(0), -500, 30, 50, "DUMMY", 2),
        Car(road.getLaneCenter(1), -600, 30, 50, "DUMMY", 2),
    ]

def reset():
    global cars, traffic, genNumber
    cars = []
    if showOnlyBestCar:
        cars = generateCars(1)
    else:
        cars = generateCars(carsPerGeneration)
    bestCar = cars[0]

    # All the cars in the traffic will be in this array
    traffic = [
        Car(road.getLaneCenter(1), -100, 30, 50, "DUMMY", 2),
        Car(road.getLaneCenter(0), -200, 30, 50, "DUMMY", 2),
        Car(road.getLaneCenter(2), -300, 30, 50, "DUMMY", 2),
        Car(road.getLaneCenter(0), -500, 30, 50, "DUMMY", 2),
        Car(road.getLaneCenter(1), -600, 30, 50, "DUMMY", 2),
    ]

    f = open("genDat.txt","w")
    f.write(str(0))
    f.close()


# initialize Pygame
pygame.init()

# set up screen
size = (800, 400)
screen = pygame.display.set_mode(size, pygame.SRCALPHA)
pygame.display.set_caption("Neural Network")

# set up game loop
done = False
clock = pygame.time.Clock()

# Create the car and other elements
road = Road(100, 200 * 0.9)
# car = Car(road.getLaneCenter(2),100,30,50, "KEYS")

if showOnlyBestCar:
    cars = generateCars(1)
else:
    cars = generateCars(carsPerGeneration)
bestCar = cars[0]

if os.path.exists("bestCar.pickle"):
    try:
        with open("bestCar.pickle", "rb") as f:
            bestCar.brain = pickle.load(f)
        f = open("genDat.txt", "r")
        genNumber = int(f.read())
        f.close()
        for i in range(len(cars)):
            for l in range(len(cars[i].brain.levels)):
                cars[i].brain.levels[l].inputs = bestCar.brain.levels[l].inputs.copy()
                cars[i].brain.levels[l].outputs = bestCar.brain.levels[l].outputs.copy()
                cars[i].brain.levels[l].biases = bestCar.brain.levels[l].biases.copy()
                for w in range(len(cars[i].brain.levels[l].weights)):
                    cars[i].brain.levels[l].weights[w] = bestCar.brain.levels[l].weights[w].copy()
            if i != 0:
                NeuralNetwork.mutate(cars[i].brain, 0.1)
        
        print(len(cars))
    except:
        print("Failed")

# All the cars in the traffic will be in this array
traffic = [
    Car(road.getLaneCenter(1), -100, 30, 50, "DUMMY", 2),
    Car(road.getLaneCenter(0), -200, 30, 50, "DUMMY", 2),
    Car(road.getLaneCenter(2), -300, 30, 50, "DUMMY", 2),
    Car(road.getLaneCenter(0), -500, 30, 50, "DUMMY", 2),
    Car(road.getLaneCenter(1), -600, 30, 50, "DUMMY", 2),


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
            if event.key == pygame.K_d:
                discard()
            if event.key == pygame.K_n:
                #save()
                next_gen()
            if event.key == pygame.K_r:
                reset()
            if event.key == pygame.K_l:
                showSensors = not showSensors
            if event.key == pygame.K_k:
                contType = not contType
                if not contType:
                    showOnlyBestCar = 1
                else:
                    showOnlyBestCar = 0
                # reset()
            if event.key == pygame.K_b:
                showOnlyBestCar = not showOnlyBestCar
                #next_gen()
            if event.key == pygame.K_t:
                randomInfiniteTraffic = not randomInfiniteTraffic

    # draw game objects
    screen.fill((211, 211, 211))

    if randomInfiniteTraffic:
        for c in range(len(traffic)):
            if traffic[c].y - bestCar.y > 200:
                traffic[c].x = road.getLaneCenter(int(random()*3))
                traffic[c].y = bestCar.y - 400

    # Check borders for all cars in traffic
    for i in range(len(traffic)):
        traffic[i].update(road.borders, [])

    # Draw the road on the screen
    road.draw(screen)

    # Draw all the cars in the traffic
    for i in range(len(traffic)):
        traffic[i].draw(screen)

    
    yMin = 1000000
    alive = carsPerGeneration
    
    for car in cars:
        if car.damaged:
            alive -= 1
        if car.y < yMin:
            yMin = car.y
            bestCar = car
        # Check collisions with borders
        car.update(road.borders, traffic)
        # Draw the car on the screen
        if not showOnlyBestCar:
            car.carImage.set_alpha(50)
            # Draw the car on the screen
            car.draw(screen)
        
    # Draw the best car on the screen
    bestCar.carImage.set_alpha(255)
    # Draw the car on the screen
    bestCar.draw(screen, showSensors)

    # Camera tracks the car
    translate(int(-bestCar.y))

    # Visualisation Of Network
    Visualizer.drawNetwork(screen, bestCar.brain)

    # pygame.draw.rect(screen, button_color, button_rect)
    # screen.blit(text, text_rect)
    
    displayTexts(screen, genNumber, carsPerGeneration, alive, showSensors, showOnlyBestCar, randomInfiniteTraffic, contType)

    # update screen
    pygame.display.flip()

    # limit FPS
    clock.tick(60)

# quit Pygame
pygame.quit()
