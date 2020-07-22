# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 02:51:11 2020

@author: Ujjaini Das
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

inputs = np.array([[0, 1, 0],
                   [0, 1, 1],
                   [0, 0, 0],
                   [1, 0, 0],
                   [1, 1, 1],
                   [1, 0, 1]])

outputs = np.array([[0], [0], [0], [1], [1], [1]])

#input_frame = pd.read_csv('training_input.csv')
#input_frame = input_frame.drop("DROP", axis = 1)
#inputs = input_frame.to_numpy()

#output_frame = pd.read_csv('training_output.csv')
#output_frame = output_frame.drop("DROP", axis = 1)
#outputs = output_frame.to_numpy()
#print(output_arr)

class NeuralNetwork:
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
        
        self.weights = np.array([[.50], [.50], [.50]])
        self.error_history = []
        self.epoch_list = []
        
    def sigmoid(self, x, deriv=False):
        if deriv == True:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))
    
    def feed_forward(self):
        self.hidden = self.sigmoid(np.dot(self.inputs, self.weights))
        
    def backpropagation(self):
        self.error = self.outputs - self.hidden
        delta = self.error * self.sigmoid(self.hidden, deriv=True)
        self.weights += np.dot(self.inputs.T, delta)
        
    def train(self, epochs=25000):
        for epoch in range(epochs):
            self.feed_forward()
            self.backpropagation()
            self.error_history.append(np.average(np.abs(self.error)))
            self.epoch_list.append(epoch)
            
    def predict(self, new_input):
        prediction = self.sigmoid(np.dot(new_input, self.weights))
        return prediction
    
NN = NeuralNetwork(inputs, outputs)
NN.train()

plt.figure(figsize=(15,5))
plt.plot(NN.epoch_list, NN.error_history)
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.show()
    