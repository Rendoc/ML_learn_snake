
import math
import random

import snake_game_ml


class SnakeML:

    def __init__(self, n_initial_games = 20, n_training_games = 20, n_moves = 20):
        self.n_initial_games = n_initial_games
        self.n_training_games = n_training_games
        self.n_moves = n_moves


    def generate_training_data(self):
        # for n_training_games
        #   play
        #   get random input
        #   [obstacle left, obstacle front, obstacle right, sugested vector(delta_x, delta_y)]
        #   output = chosen direction, 1=go with suggestion and stay alive, 0=fuck you, dead
        # after n number of games, return training data

        training_data = []

        for _ in range(self.n_initial_games):
            game = SnakeGame()
            _, _, snake, _ = game.start()

            current_situation = self.get_situation(snake)


    def get_situation(self, snake):
        #1=obstruction
        obstacle_left = self.is_direction_blocked(snake, "moJo magic")


class Model(object):
    def __init__(self):
        self.leftInputNeuron = InputNeuron(0)
        self.rightInputNeuron = InputNeuron(1)
        self.upInputNeuron = InputNeuron(0)
        self.biasInputNeuron = InputNeuron(1)
        
        list_dendrite = []
        for inputNeuron in [self.leftInputNeuron, self.rightInputNeuron, self.upInputNeuron, self.biasInputNeuron]:
            for _ in range(3):
                list_dendrite.append(Dendrite(inputNeuron))
        
        self.out_left = Neuron([list_dendrite[x] for x in range (0, 12, 3)])
        self.out_right = Neuron([list_dendrite[x] for x in range (1, 12, 3)])
        self.out_up = Neuron([list_dendrite[x] for x in range (2, 12, 3)])
    
    
    def predict(self, left, up, right):
        self.leftInputNeuron.value = left 
        self.rightInputNeuron.value = right
        self.upInputNeuron.value = up

        return [self.out_left.compute_value(), self.out_right.compute_value(), self.out_up.compute_value()]

    def train(self, data):
        # 1,1,1,(ans) ans = [0,1,1]
        for line in data:
            prediction = self.predict(line[0], line[1], line[2])
            # modifier les weight si tes proches
            if prediction line[3]

class Neuron:
    def __init__(self, vect_dendrite):
        self.vect_dendrite = vect_dendrite

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def compute_value(self):
        sum = 0
        for d in self.vect_dendrite:
            sum += d.get_value()
        return self.sigmoid(sum)

class Dendrite:
    def __init__(self, neuron: Neuron):
        self.neuron = neuron
        self.weight = random.uniform(0, 1)
    def get_value(self):
        return self.weight * self.neuron.compute_value()

class InputNeuron(Neuron):
    def __init__(self, value):
        self.value = value

    def compute_value(self):
        return self.value

if __name__ == "__main__":
    
    model = Model()
    print(model.predict(0, 1, 0))