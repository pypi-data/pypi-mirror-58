import torch
import torch.nn as nn

import functional as F


class MSELoss(nn.Module):
    def __init__(self):
        super(MSELoss, self).__init__()

    def forward(self, out, tar):
        return F.MSELoss(out, tar)


class L1Loss(nn.Module):
    def __init__(self):
        super(L1Loss, self).__init__()

    def forward(self, out, tar):
        return F.L1Loss(out, tar)