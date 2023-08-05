import numpy as np
import torch
import torch.nn as nn

def sqrt_init(shape):
    value = (1/np.sqrt(2)) * torch.ones(shape)
    return value

def complex_standard(input_centred, Vrr, Vii, Vri,
                     axis=1):
    ndim = len(input_centred.size())
    input_dim = input_centred.size()[axis] // 2
    variances_broadcast = [1]*ndim
    variances_broadcast[axis] = input_dim

    tau = Vrr + Vii
    delta = (Vrr * Vii) - (Vri ** 2)

    s = delta.sqrt()
    t = torch.sqrt(tau + 2 * s)

    invers_st = 1.0 / (s * t)
    Wrr = (Vii + s) * invers_st
    Wii = (Vrr + s) * invers_st
    Wri = -Vri * invers_st

    broadcast_Wrr = Wrr.view(variances_broadcast)
    broadcast_Wri = Wri.view(variances_broadcast)
    broadcast_Wii = Wii.view(variances_broadcast)

    cat_W_4_real = torch.cat((broadcast_Wrr,broadcast_Wii),dim=axis)
    cat_W_4_imag = torch.cat((broadcast_Wri,broadcast_Wri),dim=axis)

    input_real = input_centred[:,:input_dim]
    input_imag = input_centred[:,input_dim:]
    rolled_input = torch.cat((input_imag,input_real),dim=axis)

    output = cat_W_4_real * input_centred + cat_W_4_imag * rolled_input

    return output

def BatchNormalization(input_centred, Vrr, Vii, Vri, beta_r,
                              beta_i,gamma_rr, gamma_ri, gamma_ii, axis = 1):

    ndim = len(input_centred.size())
    input_dim = input_centred.size()[axis] // 2

    variances_broadcast = [1] * ndim
    variances_broadcast[axis] = input_dim

    standard_output = complex_standard(
        input_centred, Vrr, Vii, Vri,
        axis=axis
    )

    broadcast_gamma_rr = gamma_rr.view(variances_broadcast)
    broadcast_gamma_ii = gamma_ii.view(variances_broadcast)
    broadcast_gamma_ri = gamma_ri.view(variances_broadcast)

    cat_gamma_4_real = torch.cat((broadcast_gamma_rr, broadcast_gamma_ii),dim=axis)
    cat_gamma_4_imag = torch.cat((broadcast_gamma_ri, broadcast_gamma_ri),dim=axis)

    centred_real = standard_output[:,:input_dim]
    centred_imag = standard_output[:,input_dim:]

    rolled_output = torch.cat((centred_imag, centred_real),dim=axis)

    broadcast_beta_r = beta_r.view(variances_broadcast)
    broadcast_beta_i = beta_i.view(variances_broadcast)
    broadcast_beta = torch.cat((broadcast_beta_r,broadcast_beta_i),dim=axis)

    return cat_gamma_4_real * standard_output + cat_gamma_4_imag * rolled_output + broadcast_beta


class CBatchNorm(nn.Module):

    def __init__(self,
                 channel,
                 axis=1,
                 momentum=0.9,
                 epsilon=1e-4):
        super(BatchNorm1d, self).__init__()
        self.channel = channel
        self.axis = axis
        self.momentum = momentum
        self.epsilon = epsilon
        self.gamma_rr = nn.Parameter(sqrt_init(self.channel))
        self.gamma_ii = nn.Parameter(sqrt_init(self.channel))
        self.gamma_ri = nn.Parameter(torch.zeros(self.channel))
        self.beta_r = nn.Parameter(torch.zeros(self.channel))
        self.beta_i = nn.Parameter(torch.zeros(self.channel))

    def forward(self, input):
        input_shape = input.size()
        ndim = len(input_shape)
        input_dim = input_shape[self.axis] // 2
        reduction_axes = list(range(ndim))
        del reduction_axes[self.axis]
        mu = input.mean(dim=reduction_axes)

        broadcast_mu_shape = [1] * ndim
        broadcast_mu_shape[self.axis] = input_shape[self.axis]
        broadcast_mu = mu.view(broadcast_mu_shape)

        input_centred = input - broadcast_mu

        centred_squared = input_centred ** 2

        centred_squared_real = centred_squared[:,:input_dim]
        centred_squared_imag = centred_squared[:,input_dim:]
        centred_real = input_centred[:,:input_dim]
        centred_imag = input_centred[:,input_dim:]

        Vrr = centred_squared_real.mean(dim=reduction_axes)
        Vii = centred_squared_imag.mean(dim=reduction_axes)
        Vri = torch.mean(centred_real * centred_imag,dim=reduction_axes)

        input_bn = BatchNormalization(
            input_centred, Vrr, Vii, Vri,
            self.beta_r, self.beta_i, self.gamma_rr,
            self.gamma_ri, self.gamma_ii
        )
        return input_bn

if __name__ == "__main__":

    bn = ComplexBN(4)

    x = torch.randn(3,8,10,10)

    y= bn(x)
    print(y.size())









