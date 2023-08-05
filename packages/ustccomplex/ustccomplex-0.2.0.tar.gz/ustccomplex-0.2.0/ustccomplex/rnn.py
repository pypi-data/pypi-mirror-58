import torch
import torch.nn as nn
import numpy as np
import math

from linear import CLinear


def Ctimes(x, y):
    l = x.size(-1) // 2
    o_r = x[:, :l] * y[:, :l] - x[:, l:] * y[:, l:]
    o_i = x[:, :l] * y[:, l:] + x[:, l:] * y[:, :l]
    out = torch.cat((o_r, o_i), dim=1)
    return out


class CRNNCell(nn.Module):
    def __init__(self, input_size, hidden_size, bias=True, nonlinearity="tanh"):
        super(CRNNCell, self).__init__()
        # self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        ## Model components
        self.wih = CLinear(input_size, hidden_size, bias=bias)
        self.whh = CLinear(hidden_size, hidden_size, bias=bias)
        self.nonlinear = nn.Tanh() if nonlinearity == "tanh" else nn.ReLU()

    def forward(self, input, hx):
        x = self.wih(input)
        y = self.whh(hx)
        x = x + y
        x = self.nonlinear(x)
        return x


class CRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers=1, bias=True, nonlinearity="tanh", bidirectional="False"):
        super(CRNN, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.bias = bias
        self.nonlinear = nn.Tanh() if nonlinearity == "tanh" else nn.ReLU()
        self.layer = self._make_layer(input_size, hidden_size, num_layers, bias, nonlinearity)

    def _make_layer(self, input_size, hidden_size, num_layers, bias, nonlinearity):
        layers = []
        layers.append(CRNNCell(input_size, hidden_size, bias, nonlinearity))
        for i in range(1, num_layers):
            layers.append(CRNNCell(hidden_size, hidden_size, bias, nonlinearity))
        layer = nn.Sequential(
            CLinear(hidden_size, hidden_size, bias),
            self.nonlinear
        )
        layers.append(layer)
        return layers

    def forward(self, x, h0):
        iter = x.size(0)
        y = torch.zeros(iter, x.size(1), self.hidden_size * 2)
        hn = torch.zeros(self.num_layers, x.size(1), self.hidden_size * 2)

        xi = x[0, :, :]
        for j in range(0, self.num_layers):
            xi = self.layer[j](xi, h0[j, :, :])
            hn[j, :, :] = xi
        y[0, :, :] = self.layer[self.num_layers](xi)

        for i in range(1, iter):
            xi = x[i, :, :]
            for j in range(0, self.num_layers):
                xi = self.layer[j](xi, hn[j, :, :])
                hn[j, :, :] = xi
            y[i, :, :] = self.layer[self.num_layers](xi)
        return y, hn


class CLSTMCell(nn.Module):
    def __init__(self, input_size, hidden_size, bias=True, nonlinearity="tanh"):
        super(CLSTMCell, self).__init__()
        # self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        ## Model components
        self.uf = CLinear(input_size, hidden_size, bias=bias)
        self.wf = CLinear(hidden_size, hidden_size, bias=bias)
        self.ui = CLinear(input_size, hidden_size, bias=bias)
        self.wi = CLinear(hidden_size, hidden_size, bias=bias)
        self.ua = CLinear(input_size, hidden_size, bias=bias)
        self.wa = CLinear(hidden_size, hidden_size, bias=bias)
        self.uo = CLinear(input_size, hidden_size, bias=bias)
        self.wo = CLinear(hidden_size, hidden_size, bias=bias)
        self.nonlinear = nn.Tanh() if nonlinearity == "tanh" else nn.ReLU()
        self.theta = nn.Sigmoid()

    def forward(self, input, h_x, c_x):
        l = h_x.size(-1) // 2
        f_t = self.theta(self.wf(h_x) + self.uf(input))
        i_t = self.theta(self.wi(h_x) + self.ui(input))
        a_t = self.nonlinear(self.wa(h_x) + self.ua(input))

        c_t = Ctimes(c_x, f_t) + Ctimes(a_t, i_t)
        o_t = self.theta(self.wo(h_x) + self.uo(input))
        h_t = Ctimes(o_t, self.nonlinear(c_t))
        return h_t, c_t


class CLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers=1, bias=True, nonlinearity="tanh", bidirectional="False"):
        super(CLSTM, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.bias = bias
        self.nonlinear = nn.Tanh() if nonlinearity == "tanh" else nn.ReLU()
        self.layer = self._make_layer(input_size, hidden_size, num_layers, bias, nonlinearity)

    def _make_layer(self, input_size, hidden_size, num_layers, bias, nonlinearity):
        layers = []
        layers.append(CLSTMCell(input_size, hidden_size, bias, nonlinearity))
        for i in range(1, num_layers):
            layers.append(CLSTMCell(hidden_size, hidden_size, bias, nonlinearity))
        layer = nn.Sequential(
            CLinear(hidden_size, hidden_size, bias),
            self.nonlinear
        )
        layers.append(layer)
        return layers

    def forward(self, x, h0, c0):
        iter = x.size(0)
        y = torch.zeros(iter, x.size(1), self.hidden_size * 2)
        hn = torch.zeros(self.num_layers, x.size(1), self.hidden_size * 2)
        cn = torch.zeros(self.num_layers, x.size(1), self.hidden_size * 2)

        hi = x[0, :, :]
        for j in range(0, self.num_layers):
            hi, ci = self.layer[j](hi, h0[j, :, :], c0[j, :, :])
            hn[j, :, :] = hi
            cn[j, :, :] = ci
        y[0, :, :] = self.layer[self.num_layers](hi)

        for i in range(1, iter):
            hi = x[i, :, :]
            for j in range(0, self.num_layers):
                hi, ci = self.layer[j](hi, hn[j, :, :], cn[j, :, :])
                hn[j, :, :] = hi
                cn[j, :, :] = ci
            y[i, :, :] = self.layer[self.num_layers](hi)
        return y, hn, cn
