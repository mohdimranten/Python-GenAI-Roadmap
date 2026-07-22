
import torch

print(torch.__version__)
print(torch.cuda.is_available())   # Mac par False aayega
print(torch.backends.mps.is_available())  # Apple Silicon ho to True aana chahiye