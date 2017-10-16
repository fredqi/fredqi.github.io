---
layout: page
title: Teaching
use-site-title: false
---

# 《模式识别与应用》作业(2017-03)

## 作业提交信息

- 提交作业截止时间： 2017/11/19 23:59:59 (CST)
- 作业提交方式:
  + 发送电子邮件至 fred DOT qi AT ieee DOT org
  + 邮件标题格式： \[PRML\] HW1703-学号-姓名
- 请勿删除作业所提供代码中的注释，将你的代码放入添加代码标志中间。

### 作业提交内容

- 完善后的程序代码
- 书面报告

### 作业相关文件

- [Python 代码](/teaching/PRML/PRML_Neural_Networks.py)
- [数据文件](/teaching/PRML/PRML_NN_data.mat)
- [初始权重](/teaching/PRML/PRML_NN_weights.mat)

## 使用神经网络进行机器学习

在本项练习中，你将学会如何实现神经网络的误差反传训练算法，并应用它进行手写数字识别。

### 神经网络

#### 数据可视化

本次练习所用的数据集有5000个训练样本，每个样本对应于20x20大小的灰度图像。这些训练样本包括了9-0共十个数字的手写图像。这些样本中每个像素都用浮点数表示。加载得到的数据中，每幅图像都被展开为一个400维的向量，构成了数据矩阵中的一行。完整的训练数据是一个5000x400的矩阵，其每一行为一个训练样本（数字的手写图像）。数据中，对应于数字"0"的图像被标记为"10"，而数字"1"到"9"按照其自然顺序被分别标记为"1"到"9"。
<div>
\[X = \begin{bmatrix} - & (\mathbf{x}^{(1)})^T & - \\
                      - & (\mathbf{x}^{(2)})^T & - \\
                          &  \vdots &  \\
                      - & (\mathbf{x}^{(m)})^T & - \end{bmatrix}\]
</div>
程序的第一部分将加载数据并将其显示为如下图所示的形式。实现这一功能需要你补充完善 函数 `display_data` 。

![image](/teaching/PRML/data-array.png)

#### 模型表示

![image](/teaching/PRML/nn-representation.png)

我们准备训练的神经网络是一个三层的结构，一个输入层，一个隐层以及一个输出层。由于我们训练样本（图像）是20x20的，所以输入层单元数为400（不考虑额外的偏置项，如果考虑单元个数需要+1）。在我们的程序中，数据会被加载到变量<span> $X$ </span> 和<span> $y$ </span>里。

本项练习提供了一组训练好的网络参数<span> $(\Theta^{(1)}, \Theta^{(2)})$ </span>。这些数据存储在数据文件 `PRML_NN_weights.mat`，在程序中被加载到变量 `Theta1` 与 `Theta2` 中。参数的维度对应于第二层有25个单元、10个输出单元（对应于10个数字 的类别）的网络。

#### 前向传播与代价函数

现在你需要实现神经网络的代价函数及其梯度。首先需要使得函数 `nn_cost_function` 能够返回正确的代价值。

神经网络的代价函数（不包括正则化项）的定义为：
<div>
  \[J(\theta) = \frac{1}{m} \sum_{i=1}^{m} \sum_{k=1}^{K} \left[
     -y_k^{(i)} \log\left((h_{\theta}(x^{(i)}))_k\right)
	 -(1 - y_k^{(i)}) \log\left(1 - (h_{\theta}(x^{(i)}))_k\right) \right] \]
</div>
其中<span> $h_{\theta}(x^{(i)})$ </span> 的计算如神经网络结构图所示，<span> $K=10$ </span>是 所有可能的类别数。这里的<span> $y$ </span>使用了one-hot 的表达方式。

运行程序，使用预先训练好的网络参数，确认你得到的代价函数是正确的。（正确的代价约为0.287629）。

#### 代价函数的正则化

神经网络包括正则化项的代价函数为
<div>
\[\begin{split}
  J(\theta) =& \frac{1}{m} \sum_{i=1}^{m} \sum_{k=1}^{K} \left[
    -y_k^{(i)} \log\left((h_{\theta}(x^{(i)}))_k\right) 
    -(1 - y_k^{(i)}) \log\left(1 - (h_{\theta}(x^{(i)}))_k\right) \right] \\
	&+ \frac{\lambda}{2m} \left[ 
      \sum_{j=1}^{25} \sum_{k=1}^{400} (\Theta_{j,k}^{(1)})^2 +
      \sum_{j=1}^{10} \sum_{k=1}^{25} (\Theta_{j,k}^{(2)})^2 \right]
\end{split}\]
</div>
注意在上面式子中，正则化项的加和形式与练习中设定的网络结构一致。但是你的代码实现要保证能够用于任意大小的神经网络。
此外，还需要注意，对应于偏置项的参数不能包括在正则化项中。对于矩阵 `Theta1` 与 `Theta2` 而言，这些项对应于矩阵的第一列。

运行程序，使用预先训练好的权重数据，设置正则化系数<span> $\lambda=1$ </span>(`lmb`) 确认你得到的代价函数是正确的。（正确的代价约为0.383770）。

此步练习需要你补充实现 `nn_cost_function` 。

### 误差反传训练算法

#### `Sigmoid` 函数及其梯度

Sigmoid 函数定义为
<div>
\[\text{sigmoid}(z) = g(z) = \frac{1}{1+\exp(-z)}\]
</div>
Sigmoid 函数的梯度可以按照下式进行计算
<div>
\[g^{\prime}(z) = \frac{d}{dz} g(z) = g(z)(1-g(z))\]
</div>
为验证你的实现是正确的，以下事实可供你参考。当<span> $z=0$ </span>是，梯度的精确值为 0.25 。当<span> $z$ </span>的值很大（可正可负）时，梯度值接近于0。

这里，你需要补充完成函数 `sigmoid` 与 `sigmoid_gradient` 。 你需要保证实现的函数的输入参数可以为矢量和矩阵( `numpy.ndarray`)。

#### 网络参数的随机初始化

训练神经网络时，使用随机数初始化网络参数非常重要。一个非常有效的随机初始化策略为，在范围<span> $[ -\epsilon_{init}, \epsilon_{init} ]$ </span>内按照均匀分布随机选择参数<span> $\Theta^{(l)}$ </span>的初始值。这里你需要设置<span> $\epsilon_{init} = 0.12$ </span>。这个范围保证了参数较小且训练过程高效。

你需要补充实现函数 `rand_initialize_weigths` 。

对于一般的神经网络，如果第<span> $l$ </span>层的输入单元数为<span> $L_{in}$ </span>，输出单元数为<span> $L_{out}$ </span>，则<span> $\epsilon_{init} = {\sqrt{6}}/{\sqrt{L_{in} + L_{out}}}$ </span>可以做为有效的指导策略。

#### 误差反传训练算法 (Backpropagation)

![image](/teaching/PRML/nn-backpropagation.png)

现在你需要实现误差反传训练算法。误差反传算法的思想大致可以描述如下。对于一个训练样本<span> $(x^{(t)}, y^{(t)})$ </span>，我们首先使用前向传播计算网络中所有单元（神经元）的激活值（activation），包括假设输出<span> $h_{\Theta}(x)$ </span>。那么，对于第<span> $l$ </span>层的第<span> $j$ </span>个节点，我们期望计算出一个“误差项”<span> $\delta_{j}^{(l)}$ </span>用于衡量该节点对于输出的误差的“贡献”。

对于输出节点，我们可以直接计算网络的激活值与真实目标值之间的误差。对于我们所训练的第3层为输出层的网络，这个误差定义了<span> $\delta_{j}^{(3)}$ </span>。对于隐层单元，需要根据第<span> $l+1$ </span>层的节点的误差的加权平均来计算<span> $\delta_{j}^{(l)}$ </span>。

下面是误差反传训练算法的细节（如图3所示）。你需要在一个循环中实现步骤1至4。循环的每一步处理一个训练样本。第5步将累积的梯度除以<span> $m$ </span>以得到神经网络代价函数的梯度。

1.  设输入层的值<span> $a^{(1)}$ </span>为第<span> $t$ </span>个训练样本<span> $x^{(t)}$ </span>。执行前向传播，计算第2层与第3层各节点的激活值(<span> $z^{(2)}, a^{(2)}, z^{(3)}, a^{(3)}$ </span>)。注意你需要在<span> $a^{(1)}$ </span>与<span> $a^{(2)}$ </span>增加一个全部为 +1 的向量，以确保包括了偏置项。在 `numpy` 中可以使用函数 `ones` ， `hstack`, `vstack` 等完成（向量化版本）。
2.  对第3层中的每个输出单元<span> $k$ </span>，计算
    <div>\[\delta_{k}^{(3)} = a_{k}^{(3)} - y_k\]</div>
    其中<span> $y_k \in \{0, 1\}$ </span>表示当前训练样本是否是第<span> $k$ </span>类。

3.  对隐层<span> $l=2$ </span>, 计算
	<div>
    \[\delta^{(2)} = \left( \Theta^{(2)} \right)^T \delta^{(3)} .* g^{\prime} (z^{(2)})\]
    </div>
    其中<span> $g^{\prime}$ </span>表示 Sigmoid 函数的梯度， `.*` 在 `numpy` 中是通 常的逐个元素相乘的乘法，矩阵乘法应当使用 `numpy.dot` 函数。

4.  使用下式将当前样本梯度进行累加：
	<div>
    \[\Delta^{(l)} = \Delta^{(l)} + \delta^{(l+1)}(a^{(l)})^T\]
	</div>
    在 `numpy` 中，数组可以使用 `+=` 运算。

5.  计算神经网络代价函数的（未正则化的）梯度，
	<div>
    \[\frac{\partial}{\partial \Theta_{ij}^{(l)}} J(\Theta) = D_{ij}^{(l)} = \frac{1}{m} \Delta_{ij}^{(l)}\]
	</div>

这里，你需要（部分）完成函数 `nn_grad_function` 。程序将使用函数 `check_nn_gradients` 来检查你的实现是否正确。在使用循环的方式完成函数 `nn_grad_function` 后，建议尝试使用向量化的方式重新实现这个函数。

#### 检查梯度

在神经网络中，需要最小化代价函数<span> $J(\Theta)$ </span>。为了检查梯度计算是否正确，考虑把参数<span> $\Theta^{(1)}$ </span>和<span> $\Theta^{(2)}$ </span>展开为一个长的向量<span> $\theta$ </span>。假设函数<span> $f_i(\theta)$ </span>表示<span> $\frac{\partial}{\partial \theta_i} J(\theta)$ </span>。

令
<div>
\[\theta^{(i+)} = \theta + \begin{bmatrix} 0 \\ 0 \\ \vdots \\ \epsilon \\ \vdots \\ 0 \end{bmatrix} \qquad
  \theta^{(i-)} = \theta - \begin{bmatrix} 0 \\ 0 \\ \vdots \\ \epsilon \\ \vdots \\ 0 \end{bmatrix}\]
</div>
上式中，<span> $\theta^{(i+)}$ </span>除了第<span> $i$ </span>个元素增加了<span> $\epsilon$ </span>之 外，其他元素均与<span> $\theta$ </span>相同。类似的，<span> $\theta^{(i-)}$ </span>中仅第<span> $i$ </span>个元素减少了<span> $\epsilon$ </span>。可以使用数值近似验证<span> $f_i(\theta)$ </span>计算是否正确：
<div>
\[f_i(\theta) \approx \frac{J(\theta^{(i+)}) - J(\theta^{(i-)})}{2\epsilon}\]
</div>
如果设<span> $\epsilon=10^{-4}$ </span>，通常上式左右两端的差异出现于第4位有效数字之后（经常会有更高的精度）。

在练习的程序代码中，函数 `compute_numerical_gradient` 已经实现，建议你认真阅读该函数并理解其实现原理与方案。

之后，程序将执行 `check_nn_gradients` 函数。该函数将创建一个较小的神经网络用于检测你的误差反传训练算法所计算得到的梯度是否正确。如果你的实现是正确的，你得到的 梯度与数值梯度之后的绝对误差（各分量的绝对值差之和）应当小于<span> $10^{-9}$ </span>。

#### 神经网络的正则化

你正确实现了误差反传训练算法之后，应当在梯度中加入正则化项。

假设你在误差反传算法中计算了<span> $\Delta_{ij}^{(l)}$ </span>，你需要增加的正则化项为
<div>
\[\frac{\partial}{\partial \Theta_{ij}^{(l)}} J(\Theta) = D_{ij}^{(l)} = \frac{1}{m} \Delta_{ij}^{(l)} \qquad \text{for } j = 0\]
\[\frac{\partial}{\partial \Theta_{ij}^{(l)}} J(\Theta) = D_{ij}^{(l)} = \frac{1}{m} \Delta_{ij}^{(l)} + \frac{\lambda}{m} \Theta_{ij}^{(l)} \qquad \text{for } j \geq 1\]
</div>
注意你不应该正则化<span> $\Theta^{(l)}$ </span>的第一列，因其对应于偏置项。

此步练习需要你补充实现函数 `nn_grad_function` 。

#### 使用 `fmin_cg` 学习网络参数

如果你正确实现了神经网络的代价函数与梯度计算函数，下一步就是使用 `scipy.optimize.fmin_cg` 函数学习一组较好的网络参数。

在训练完成后，程序会汇报在训练集上的正确率。如果你的实现正确，得到的正确率应该在 95.4% 左右（由于随机初始化的原因可能有 1% 变化）。

你可以调整正则化参数<span> $\lambda$ </span>(`lmb`) 以及优化算法的最大迭代次数（如设 `maxiter = 400` ），来观察各参数对训练过程和结果的影响。

### 可视化隐层

理解神经网络学到什么的一种途径是将隐层单元学到的表示进行可视化。非正式的说，对一个特定的隐层单元，一种可视化其计算结果的方式是找到一个能够使其激活（即其activation value <span> $a_{i}^{(l)}$ </span>接近于1）输入<span> $\mathbf{x}$ </span>。

对于我们学得的神经网络，一种可视化其隐层所学得的“表示”的方式是将除偏置单元外的 400 维向量转换为 20x20 的图像并显示出来。
