# A tensor is a multi-dimensional Array that is the fundamental data-Structure uses in Pytorch.

# import torch

# tensor_1d = torch.tensor([7,8,9])
# tensor_2d = torch.tensor([[1,28],[3,84]])
# tensor_3d = torch.tensor([[6,7],[54,5],[57,67]])

# random_tensor  = torch.rand(3,3)
# print("random Tensor (2X3):",random_tensor)
# zero_tensor = torch.zeros(3,3)
# print("Zeros Tensor (2x3) :")
# print(zero_tensor)

# ones_tensor = torch.ones(3,3)
# print(ones_tensor)


# import torch

# tensor  = torch.tensor([[1,2],[3,4],[5,6]])
# elem = tensor[2,1]
# print(f"Indexed element (Row 1,Column 0): {elem}")

# reshaped_tensor = tensor.view(2,3)

# print(reshaped_tensor)


import torch

a = torch.tensor([[1, 2, 3], [4, 5, 6],[1,2,3],[4,67,77]])
b = torch.tensor([[10,30,50]])

broadcasted_result = a + b
print(broadcasted_result)
print()