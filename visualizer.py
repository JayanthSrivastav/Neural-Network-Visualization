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
        
        levelHeight = height/len(network.levels)
        
        # draw the black background
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(200,0,400,400))
        
        for i in range(len(network.levels)-1, -1, -1):
            if len(network.levels) == 1:
                levelTop = top + lerp(height - levelHeight, 0, 0.5)
            else:
                levelTop = top + lerp(height - levelHeight, 0, i/(len(network.levels)-1))
            
            if i == len(network.levels) - 1:
                Visualizer.drawLevel(screen, network.levels[i], left, levelTop, width, levelHeight, ['🠉','🠈','🠊','🠋'])

            Visualizer.drawLevel(screen, network.levels[i], left, levelTop, width, levelHeight, [])


        
    
    def drawLevel(screen, level, left, top, width, height, outputLables):
       
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
                # Draw the text surface onto the Pygame display surface at coordinates (100, 100)
            x = (Visualizer.getNodeX(outputs, i, left, right)) + 200
            pygame.draw.circle(screen, (0,0,0), (x, top), nodeRadius)
            pygame.draw.circle(screen, getRGBA(outputs[i]), (x, top), nodeRadius * 0.6)
            pygame.draw.circle(screen, getRGBA(biases[i]), (x, top), nodeRadius * 0.8, 2)
        

    def getNodeX(nodes, index, left, right):
        return lerp(left, right, index/(len(nodes) - 1))
