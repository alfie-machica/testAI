import numpy as np


X = [[1, 2, 3, 2.5],
          [2, 5, -1, 2, ],
          [-1.5, 2.7, 3.3, -0.8, ]]

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_Dense(4, 1500000000)
layer2 = Layer_Dense(1500000000, 2)

print ("done")