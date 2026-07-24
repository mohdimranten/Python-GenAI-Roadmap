# Student Marks Prediction using Neural Network

# import Libraries
import torch
import torch.nn as nn
import torch.optim as optim

#Create Dataset
x = torch.tensor([[1.0],
                  [2.0],
                  [3.0],
                  [4.0],
                  [5.0],
                  [6.0]
                  ])

y = torch.tensor([[35.0],
                  [45.0],
                  [55.0],
                  [65.0],
                  [75.0],
                  [85.0]
                  ])


#Create Model
model = nn.Linear(1,1)

#Loss Function
loss_fn = nn.MSELoss()

#Optimizer
optimizer = optim.SGD(model.parameters(),lr=0.01)

#Training
epochs = 500

for epoch in range(epochs):
    prediction = model(x)
    loss = loss_fn(prediction,y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if(epoch + 1) % 50 == 0: 
        print(f"Epoch {epoch+1}, Loss = {loss.item():.4f}")


# Prediction 
test = torch.tensor([[7.0]])
prediction = model(test)

print("\nPrediction Marks: ", prediction.item())

print("Weight: ", model.weight.item())
print("Bias: ", model.bias.item())