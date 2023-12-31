inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0, ],
           [0.5, -0.91, 0.26, -0.5, ],
           [-0.26, -0.27, 0.17, 0.87, ]]
biases = [2, 3, 0.5]

layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for  n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

# print (layer_outputs)

######dot product
import numpy as np

# weights = weights[0]
# bias = biases[0]
# output = np.dot(weights, inputs) + bias
# print (output)

output = np.dot(weights, inputs) + biases
# print (output)

######part 4
inputs = [[1, 2, 3, 2.5],
          [2, 5, -1, 2, ],
          [-1.5, 2.7, 3.3, -0.8, ]]

weights2 = [[.1, -0.14, 0.5, ],
            [-0.5, 0.12, -0.33,],
            [-0.44, 0.73, -0.13, ]]
biases2 = [-1, 2, -0.5]
layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2
print (layer2_outputs)