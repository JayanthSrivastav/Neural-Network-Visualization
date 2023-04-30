import pygame
from car import *
from road import *
from visualizer import *
import pickle


showOnlyBestCar = 0
carsPerGeneration = 500

def generateCars(N):
    cars = []
    for i in range(1, N+1):
        cars.append( Car(road.getLaneCenter(1),100,30,50,"AI"))
    return cars

def save():
    global bestCar
    with open("bestCar.pickle", "wb") as f:
        pickle.dump(bestCar.brain, f)

def discard():
    pass



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
# car = Car(road.getLaneCenter(2),100,30,50, "KEYS")

if showOnlyBestCar:
    cars = generateCars(1)
else:
    cars = generateCars(carsPerGeneration)
bestCar = cars[0]
try:
    with open("bestCar.pickle", "rb") as f:
        bestCar.brain = pickle.load(f)
    for i in range(len(cars)):
        cars[i].brain = bestCar.copy()

        if i != 0:
            NeuralNetwork.mutate(cars[i].brain, 0.9)
    
    print(len(cars))
except:
    pass

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
            if event.key == pygame.K_d:
                discard()

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

    
    yMin = 1000000
    for car in cars:
        if car.y < yMin:
            yMin = car.y
            bestCar = car
        # Check collisions with borders
        car.update(road.borders, traffic)
        # Draw the car on the screen
        car.carImage.set_alpha(50)
        # Draw the car on the screen
        car.draw(screen)
        
    # Draw the best car on the screen
    bestCar.carImage.set_alpha(255)
    # Draw the car on the screen
    bestCar.draw(screen, True)

    # Camera tracks the car
    translate(int(-bestCar.y))

    # Visualisation Of Network
    Visualizer.drawNetwork(screen, bestCar.brain)
    
    # pygame.draw.rect(screen, button_color, button_rect)
    # screen.blit(text, text_rect)
    
    # update screen
    pygame.display.flip()

    # limit FPS
    clock.tick(60)

# quit Pygame
pygame.quit()
