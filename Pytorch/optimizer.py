import torch
import torch.nn as nn
import torch.optim as optim


x = torch.tensor([[1.0],
                   [2.0],
                   [3.0],
                   [4.0]])

y = torch.tensor([[3.0],
                  [5.0],
                  [7.0],
                  [9.0]])


model = nn.Linear(1,1)

loss_fn = nn.MSELoss()

optimizer = optim.SGD(model.parameters(), lr=0.01)

epochs = 100
for epoch in range(epochs):

    prediction = model(x)
    loss = loss_fn(prediction,y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if(epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1:3d} | Loss = {loss.item():4f}")