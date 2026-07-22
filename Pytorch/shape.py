# Program 1
# Create a tensor with values 1–10.

import torch
x = torch.tensor([1,2,3,4,5,6,7,8,9,10])
print("Tensor: ",x)


# Program 2
# Print tensor shape.
print("Shape: ",x.shape)


# Program 3
# Print tensor dimensions.
print("Dimensions: ",x.ndim)


# Program 4
# Print tensor datatype.
print("Data Type: ",x.dtype)


# Program 5
# Print tensor device.

print("Device: ",x.device)

# Program 6
# Print number of elements.
print("Number of Elements:", x.numel())


# Program 7
# Print maximum value.
print("Maximum: ", x.max())

# Program 8
# Print minimum value.

print("Minimum: ",x.min())


# Program 9
# Print sum.

print("Sum: ",x.sum())

# Program 10
# Print mean.

# Hint: Integer tensor ke liye pehle float me convert karein:
print("Mean: ",x.float().mean())

# Program 11
# Create two tensors and add them.

a = torch.tensor([1,2,3])
b = torch.tensor([4,5,6])
x = a+b
print("Addition: ",x)

# Program 12
# Subtract two tensors.
x = a-b
print("Subtraction: ",x)


# Program 13
# Multiply two tensors.
x = a*b
print("Multi: ",x)


# Program 14
# Divide two tensors.
x = a/b
print("Divide: ",x)


# Program 15
# Create two matrices and perform matrix multiplication.

a = torch.tensor([
    [1,2,3],
    [4,5,6]
])      # Shape (2,3)

b = torch.tensor([
    [7,8],
    [9,10],
    [11,12]
])      # Shape (3,2)

x = torch.matmul(a, b)
print(x)


# Program 16
# Transpose a matrix.
a = torch.tensor([
    [1,2,3],
    [4,5,6]
])

x= a.T
print(x)


# Program 17
# Create a random 4×4 tensor.
x = torch.rand(4,4)
print(x)


# Program 18
# Create a 3×3 zeros tensor.
x = torch.zeros(3,3)
print(x)