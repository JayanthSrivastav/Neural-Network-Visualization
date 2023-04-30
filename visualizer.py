from utils import *
import pygame
import math

class Visualizer:
    def drawNetwork( screen, network):
        margin = 50
        left = margin
        top = margin
        width = 400 - margin*2
        height = 400 - margin * 2
        


        Visualizer.drawLevel(screen, network.levels[0], left, top, width, height)
    
    def drawLevel(screen, level, left, top, width, height):
        # draw the black background
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(200,0,400,400))
        right = left + width
        bottom = top + height

        inputs = level.inputs
        
        outputs = level.outputs
        weights = level.weights     
        biases = level.biases   

        nodeRadius = 18
        for i in range(len(inputs)):
            for j in range(len(outputs)):
                value = weights[i][j]
                pygame.draw.line(screen, getRGBA(value), (Visualizer.getNodeX(inputs, i, left, right) + 200, bottom), (Visualizer.getNodeX(outputs, j, left, right)+ 200, top))

        for i in range(len(inputs)):
            x = Visualizer.getNodeX(inputs, i, left, right) + 200
            pygame.draw.circle(screen, (0,0,0), (x, bottom), nodeRadius)
            pygame.draw.circle(screen, getRGBA(inputs[i]), (x, bottom), nodeRadius * 0.6)

        for i in range(len(outputs)):
            x = (Visualizer.getNodeX(outputs, i, left, right)) + 200
            pygame.draw.circle(screen, (0,0,0), (x, top), nodeRadius)
            pygame.draw.circle(screen, getRGBA(outputs[i]), (x, top), nodeRadius * 0.6)
            pygame.draw.circle(screen, getRGBA(biases[i]), (x, top), nodeRadius * 0.8, 2)

    def getNodeX(nodes, index, left, right):
        return lerp(left, right, index/(len(nodes) - 1))
