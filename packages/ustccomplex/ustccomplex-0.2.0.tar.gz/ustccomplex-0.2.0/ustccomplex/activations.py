import torch
import torch.nn as nn
import functional as F


class CSin(nn.Module):
    def __init__(self):
        super(CSin, self).__init__()

    def forward(self, x):
        return F.sinz(x)


class CTan(nn.Module):
    def __init__(self):
        super(CTan, self).__init__()

    def forward(self, x):
        return F.tanz(x)


class CTanh(nn.Module):
    def __init__(self):
        super(CTanh, self).__init__()

    def forward(self, x):
        return F.tanhz(x)


class CSinh(nn.Module):
    def __init__(self):
        super(CSinh, self).__init__()

    def forward(self, x):
        return F.sinhz(x)