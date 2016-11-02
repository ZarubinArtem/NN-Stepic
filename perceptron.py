# basic crap Perceptron

from numpy import array

class Perceptron:

    def __init__(self, X, weights, bias):
        self.X = array(X)
        self.weights = array(weights)
        self.bias = bias

    def fire(self):
        response = sum(self.X * self.weights) + self.bias
        if response > 0:
            return 1, response
        else:
            return 0, response


P = Perceptron([1,1,1], [0.9, 0.2, 0.1], 0.05)
print(P.fire())
