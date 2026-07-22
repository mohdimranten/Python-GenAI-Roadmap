# Create a scalar tensor.
import torch
x = torch.tensor(4)
print("Tensor: ",x)
print("Size :",x.shape)
print("Dimensions: ",x.ndim)
print("-----------------------")


# Create a vector of 10 numbers.
import torch
x = torch.tensor([2,3,4,5,6,7,8,9,10,8])
print("Tensor: ",x)
print("Size:", x.shape)
print("Dimensions: ",x.ndim)
print("-----------------------")

# Create a 3×3 matrix.
import torch
x = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
print("Tensor: ",x)
print("Size: ",x.shape)
print("Dimensions: ",x.ndim)
print("-----------------------")



# Create a 2×2×2 tensor.
import torch
x = torch.tensor([
    [
        [1,2],
        [3,4]
    ],
    [   
        [5,6],
        [7,8]
    ]]
)
print("Tensor: ",x)
print("Size: ",x.shape)
print("Dimensions: ",x.ndim)
print("-----------------------")
# Create a 5×5 zeros tensor.

import torch
x = torch.zeros(5,5)
print("Tensor",x)
print("Size: ",x.shape)
print("Dimensions: ", x.ndim)
print("-----------------------")
# Create a 4×4 ones tensor.

import torch
x = torch.ones(4,4)
print("Tensor: ",x)
print("Size",x.shape)
print("Dimensions: ",x.ndim)
print("-----------------------")

# Generate a random 2×5 tensor.

import torch
x = torch.rand(2,5)
print("Tensor: ",x)
print("Size: ",x.shape)
print("Dimensions: ",x.ndim)
print("-----------------------")

# Create a 6×6 identity matrix.
import torch
x = torch.eye(6)
print("Tensor: ",x)
print("Size: ",x.shape)
print("Dimensions: ",x.ndim)
print("-----------------------")
# Add two tensors.
a = torch.tensor([1,2,3])
b = torch.tensor([4,4,5])
x = a+b
print("Tensor: ",x)
print("Size: ",x.shape)
print("Dimensions: ",x.ndim)
print("-----------------------")
# Subtract two tensors.
a = torch.tensor([5,6,7])
b = torch.tensor([8,9,8])

x = b-a
print("Tensor: ",x)
print("Size: ",x.shape)
print("Dimensions: ",x.ndim)
print("-----------------------")
# Multiply two tensors element-wise.

import torch
a = torch.tensor([4,5,6])
b = torch.tensor([5,5,6])
x = a*b
print("Tensor: ",x)
print("Size: ",x.shape)
print("Dimensions: ",x.ndim)
print("-----------------------")
# Divide two tensors.

import torch
a = torch.tensor([15,24,7])
b = torch.tensor([5,6,7])
x = a/b
print("Tensor: ",x)
print("Size: ", x.shape)
print("Dimensions: ",x.ndim)
print("-----------------------")
# Perform matrix multiplication.
import torch
a = torch.tensor([

    [1,2],
    [3,4]
])


b = torch.tensor([
    [4,5],
    [6,7]
])

x = torch.matmul(a,b)
print("Tensor: ",x)
print("Size: ",x.shape)
print("Dimensions: ",x.ndim)
print("-----------------------")

# Find the transpose of a matrix.
import torch
a = torch.tensor([
    [1,2,3],
    [4,5,6]
])
x = a.T
print("Tensor: ",x)
print("Size: ",x.shape)
print("Dimensions: ",x.ndim)
print("-----------------------")

# Print a tensor's shape, dimensions, data type, minimum value, and maximum value.
import torch
x = torch.tensor([4,5,6,7,8])
print("Size: ",x.shape)
print("Dimensions: ",x.ndim)
print("Data Type: ",x.dtype)
print("Minimum Value: ",x.min())
print("Maximum Value: ",x.max())
print("-----------------------")