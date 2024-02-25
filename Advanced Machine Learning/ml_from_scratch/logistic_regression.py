# Create a new Python file, e.g.
# Copy the provided script below and save it.

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def model(X, Y, learning_rate, iterations):
    
    m = X.shape[1]
    n = X.shape[0]
    
    W = np.zeros((n, 1))
    B = 0
    
    cost_list = []
    
    for i in range(iterations):
        
        Z = np.dot(W.T, X) + B
        A = sigmoid(Z)
        
        # cost function
        cost = -(1/m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))
        
        # Gradient Descent
        dW = (1/m) * np.dot(A - Y, X.T)
        dB = (1/m) * np.sum(A - Y)
        
        W = W - learning_rate * dW.T
        B = B - learning_rate * dB
        
        # Keeping track of our cost function value
        cost_list.append(cost)
        
        if i % (iterations / 10) == 0:
            print("Cost after", i, "iteration is:", cost)
        
    return W, B, cost_list
