import warnings
import math

import torch
import torch.nn as nn

def tanz(z):
    batch = z.size(0)
    feature = z.size(1) // 2
    length = z.size(2)
    for i in range(0, batch):
        for j in range(0, feature):
            for k in range(0, length):
                a = z[i, j, k]
                b = z[i, j+feature, k]
                e_2b = math.exp(2*b)
                cosa = math.cos(a)
                sina = math.sin(a)
                norm = ((e_2b + 1)*cosa)**2 + ((e_2b - 1)*sina)**2
                z[i, j, k] = (4*e_2b*cosa*sina)/norm
                z[i, j+feature, k] = (e_2b**2- 1)/norm
    return z

def sinz(z):
    batch = z.size(0)
    feature = z.size(1) // 2
    length = z.size(2)
    for i in range(0, batch):
        for j in range(0, feature):
            for k in range(0, length):
                a = z[i, j, k]
                b = z[i, j+feature, k]
                e_b = math.exp(b)
                e_b2 = math.exp(-b)
                cosa = math.cos(a)
                sina = math.sin(a)
                z[i, j, k] = (e_b + e_b2) * sina / 2
                z[i, j+feature, k] = (e_b - e_b2) * cosa / 2
    return z

def tanhz(z):
    batch = z.size(0)
    feature = z.size(1) // 2
    length = z.size(2)
    for i in range(0, batch):
        for j in range(0, feature):
            for k in range(0, length):
                a = z[i, j, k]
                b = z[i, j+feature, k]
                e_2a = math.exp(2*a)
                cosb = math.cos(b)
                sinb = math.sin(b)
                norm = ((e_2a + 1)*cosb)**2 + ((e_2a - 1)*sinb)**2
                z[i, j, k] = (e_2a**2- 1)/norm
                z[i, j+feature, k] = (4*e_2a*cosb*sinb)/norm
    return z

def sinhz(z):
    batch = z.size(0)
    feature = z.size(1) // 2
    length = z.size(2)
    for i in range(0, batch):
        for j in range(0, feature):
            for k in range(0, length):
                a = z[i, j, k]
                b = z[i, j+feature, k]
                e_a = math.exp(a)
                e_a2 = math.exp(-a)
                cosb = math.cos(b)
                sinb = math.sin(b)
                z[i, j, k] = (e_a - e_a2) * cosb / 2
                z[i, j+feature, k] = (e_a + e_a2) * sinb / 2
    return z


def MSELoss(out, tar):
    input_dim = out.size(1) // 2
    a = (tar[:, :input_dim]-out[:, :input_dim])**2+(tar[:, input_dim:]-out[:, input_dim:])**2

    return torch.sum(a, 1) / input_dim


def L1Loss(out, tar):
    input_dim = out.size(1) // 2
    a = (tar[:, :input_dim] - out[:, :input_dim]) ** 2 + (tar[:, input_dim:] - out[:, input_dim:]) ** 2
    b = torch.sqrt(a)
    return torch.sum(b, 1) / input_dim
