#READ ME

本函数包的搭建基于pytorch平台，函数名定义格式均为：C+pytorch函数名，如：
**CConv1d**

类与函数的具体使用方式可以参考pytorch文档，区别在于我们实现了对于复值输入的复域上的运算。

我们对于复数输入的格式有以下三种定义

- 在卷积神经网络中，input = [batch ,（channel×2) , input_size ]
- 在无channel参数的函数中，如：计算复数模长的函数*CNorm*，复值全连接层*CLinear*中， input=[batch,(input_size×2)]
- 在RNN、LSTM、GRU中，input = [seq_len, batch, (input_size×2)]