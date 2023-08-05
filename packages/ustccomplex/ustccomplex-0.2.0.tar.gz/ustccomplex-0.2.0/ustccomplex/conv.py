# -*- coding: utf-8 -*-
import torch
import torch.nn as nn
import numpy as np

class CConv1d(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True):
        super(CConv1d, self).__init__()
        #self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        #self.padding = padding

        ## Model components
        self.conv_re = nn.Conv1d(in_channels, out_channels, kernel_size, stride=stride, padding=padding, dilation=dilation, groups=groups, bias=bias)
        self.conv_im = nn.Conv1d(in_channels, out_channels, kernel_size, stride=stride, padding=padding, dilation=dilation, groups=groups, bias=bias)


    def forward(self, x): # shpae of x : [batch,channel*2,axis1,axis2]

        input_dim = x.size()[1] // 2
        real = self.conv_re(x[:,:input_dim]) - self.conv_im(x[:,input_dim:])
        imaginary = self.conv_re(x[:,input_dim:]) + self.conv_im(x[:,:input_dim])
        output = torch.cat((real,imaginary),dim=1)
        return output

class CConv2d(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True):
        super(CConv2d, self).__init__()
        #self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        #self.padding = padding

        ## Model components
        self.conv_re = nn.Conv2d(in_channels, out_channels, kernel_size, stride=stride, padding=padding, dilation=dilation, groups=groups, bias=bias)
        self.conv_im = nn.Conv2d(in_channels, out_channels, kernel_size, stride=stride, padding=padding, dilation=dilation, groups=groups, bias=bias)


    def forward(self, x): # shpae of x : [batch,channel*2,axis1,axis2]

        input_dim = x.size()[1] // 2
        real = self.conv_re(x[:,:input_dim]) - self.conv_im(x[:,input_dim:])
        imaginary = self.conv_re(x[:,input_dim:]) + self.conv_im(x[:,:input_dim])
        output = torch.cat((real,imaginary),dim=1)
        return output

class CConv3d(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True):
        super(CConv3d, self).__init__()
        #self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        #self.padding = padding

        ## Model components
        self.conv_re = nn.Conv3d(in_channels, out_channels, kernel_size, stride=stride, padding=padding, dilation=dilation, groups=groups, bias=bias)
        self.conv_im = nn.Conv3d(in_channels, out_channels, kernel_size, stride=stride, padding=padding, dilation=dilation, groups=groups, bias=bias)


    def forward(self, x): # shpae of x : [batch,channel*2,axis1,axis2]

        input_dim = x.size()[1] // 2
        real = self.conv_re(x[:,:input_dim]) - self.conv_im(x[:,input_dim:])
        imaginary = self.conv_re(x[:,input_dim:]) + self.conv_im(x[:,:input_dim])
        output = torch.cat((real,imaginary),dim=1)
        return output



#%%
if __name__ == "__main__":
    ## Random Tensor for Input
    ## shape : [batchsize,2*channel,axis1_size,axis2_size]
    ## Below dimensions are totally random
    x = nn.Parameter(torch.ones(2))



    real = x[0] - x[1]
    imaginary = x[0] + x[1]
    output = real**2+imaginary**2

    print(output)
    output.backward()
    print(x.grad)


    
    # 1. Make ComplexConv1d Object
    ## (in_channels, out_channels, kernel_size) parameter is required



