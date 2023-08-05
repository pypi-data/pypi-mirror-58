import torch
import numpy

def CNorm(x):

    input_dim = x.size()[1] // 2

    re = x[:, :input_dim]
    im = x[:, input_dim:]
    abs = torch.sqrt(re * re + im * im)

    return abs

if __name__ == "__main__":

    a = torch.ones(2, 2, 2)
    print(ComplexAbs(a))
