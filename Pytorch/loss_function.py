# 1. Mean Squared Error (MSE)

# MSE is mainly used for Regression problems.

# Examples:

# House Price Prediction
# Salary Prediction
# Temperature Prediction
# Stock Price Prediction

# Formula: MSE = 1/n ​i=1∑n​(yi​−y^​i​)2 

#MSE Example

import torch 
import torch.nn as nn
 
loss_fn = nn.MSELoss() 
prediction = torch.tensor([2.5])
target = torch.tensor([3.0])

loss = loss_fn(prediction,target)

print("Mean Squared Error: ", loss)
print("\n")
##########################################

# Multiple value

import torch
import torch.nn as nn

loss_fn = nn.MSELoss()
prediction = torch.tensor([4.0,7.0,10.0])
target = torch.tensor([1.0,3.0,5.0])

loss = loss_fn(prediction,target)

print("Mean Squared Error: ", loss)

# 2. Cross Entropy Loss

# Cross Entropy is used for Classification problems.

# Examples:

# Cat vs Dog
# Spam Detection
# Disease Prediction
# Digit Recognition (MNIST)

import torch
import torch.nn as nn

loss_fn = nn.CrossEntropyLoss()
prediction = torch.tensor([2.0,1.0,0.1])
target = torch.tensor([0])

loss = loss_fn(prediction,target)
print(loss)

################################

# program 1 

import torch
import torch.nn as nn

loss_fn = nn.MSELoss()

# program 2
import torch
import torch.nn as nn

loss_fn = nn.MSELoss()
prediction = torch.tensor([4.0])
target = torch.tensor([2.0])
loss = loss_fn(prediction,target)

print("Mean Squred Error: ", loss)