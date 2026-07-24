import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()



# Linear Layer
# A Linear layer is a Fully Connected(Dense) Layer  
import torch
import torch.nn as nn

layer = nn.Linear(3, 2)

x = torch.tensor([[1.0, 2.0, 3.0]])

output = layer(x)

print(output)


# Example of Simple Neural Network

import torch
import torch.nn as nn

class SimpleNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(3,4)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(4,1)

    def forward(self, x):

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x

model = SimpleNN()

print(model)