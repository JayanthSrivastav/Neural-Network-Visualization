from random import random

# Main NeuralNetwork class
class NeuralNetwork:
    def __init__(self, neuronCounts):
        self.levels = []
        for i in range(len(neuronCounts)-1):
            self.levels.append(Level(neuronCounts[i], neuronCounts[i+1]))

    def feedForward(givenInputs, network):
        outputs = Level.feedForward(givenInputs, network.levels[0])
        
        for i in range(1,len(network.levels)):
            outputs = Level.feedForward(outputs, network.levels[i])

        return outputs

# Level class for input and output layer levels
class Level:
    def __init__(self, inputCount, outputCount):
        self.inputs = [0] * inputCount
        self.outputs = [0] * outputCount
        self.biases = [0] * outputCount

        self.weights = [0] * inputCount

        for i in range(inputCount):
            self.weights[i] = [0] * outputCount 

        Level.randomize(self)

    def randomize(level):
        for i in range(len(level.inputs)):
            for j in range(len(level.outputs)):
                level.weights[i][j] = random()*2 - 1;

        for i in range(len(level.biases)):
            level.biases[i] = random()*2 - 1

    # Feedforward Algorithm
    def feedForward(givenInputs, level):

        for i in range(len(level.inputs)):
            level.inputs[i] = givenInputs[i]
        # print(givenInputs)
        for i in range(len(level.outputs)):
            s = 0
            for j in range(len(level.inputs)):
                s += level.inputs[j] * level.weights[j][i]

            if(s>level.biases[i]): # if(s + level.biases[i]>0):
                level.outputs[i] = 1
            else:
                level.outputs[i] = 0

        return level.outputs
