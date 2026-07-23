# import torch

# x = torch.tensor(5.0, requires_grad=True)

# print("Input: ",x)

# y = x**2
# print("OutPut: ",y)

# y.backward()
# print("Grad: ",x.grad)

# # second 2

# import torch
# x = torch.tensor(2.0, requires_grad=True)
# print("Input: ",x)

# y = 3 * x + 5
# y.backward()

# print("Gradient: ",x.grad)


# Gradient of y = x²
import torch
x = torch.tensor(2.0,requires_grad=True)
print("Input: ",x)
y = x**2
y.backward()
print("Gradient: ",x.grad)

# Gradient of y = x³
import torch
x = torch.tensor(2.0,requires_grad=True)
print("Input: ",x)
y = x**3
y.backward()
print("Gradient: ",x.grad)

# Gradient of y = 5x + 10

import torch
x = torch.tensor(2.0,requires_grad=True)
print("Input: ",x)
y = 5 * x + 10
y.backward()
print("Gradient:",x.grad)


# Gradient of y = x² + 3x + 1
import torch
x = torch.tensor(2.0,requires_grad=True)
print("Input: ",x)
y = x**2 + 3 * x + 1
y.backward()
print("Gradient: ",x.grad) 
print("\n")

# Print grad_fn
import torch
x = torch.tensor(2.0,requires_grad=True)
print("Input: ",x)
y = x**2
y.backward()
print("Output:",y)
print("Gradient:",x.grad)
print("grad_fn",y.grad_fn)
print("\n")


# Demonstrate gradient accumulation
import torch
x = torch.tensor(2.0, requires_grad=True)
print("Input: ",x)
y = x ** 2
y.backward()
print("Gradient: ",x.grad)

z = x ** 3
z.backward()
print("Gradient: ",x.grad)

v = x ** 2
v.backward()
print("Gradient: ",x.grad) 

# Reset gradients using x.grad.zero_()
import torch
x = torch.tensor(2.0,requires_grad=True)
print("Input: ",x)
y = x**2
y.backward()
print("Gradient: ", x.grad)

x.grad.zero_()
print("After Zero: ",x.grad)

# Use detach()
# Use torch.no_grad()
# Create your own function and verify the gradient manually.