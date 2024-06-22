import torch
import torch.nn as nn


# Implement the Softmax class
class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / torch.sum(exp_x)


# Implement the SoftmaxStable class
class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        c = torch.max(x)
        exp_x = torch.exp(x - c)
        return exp_x / torch.sum(exp_x)


# Create some example input
data = torch.Tensor([1, 2, 3])

# Instantiate and use the Softmax class
softmax = Softmax()
output = softmax(data)
print("Softmax output:", output)

# Instantiate and use the SoftmaxStable class
softmax_stable = SoftmaxStable()
output_stable = softmax_stable(data)
print("SoftmaxStable output:", output_stable)
