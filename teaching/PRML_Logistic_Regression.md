---
layout: page
title: 《模式识别与应用》作业(2017-02)
subtitle: Teaching
mathjax: true
---

在本次作业中，你将实现逻辑回归算法，并将之应用于两个数据集。

# 作业提交信息

- 提交作业截止时间： 2017/11/02 23:59:59 (CST)
- 作业提交方式:
  + 邮件标题格式： \[PRML\] HW1702-学号-姓名
  + 发送电子邮件至 fred DOT qi AT ieee DOT org
- 请勿删除作业所提供代码中的注释，将你的代码放入添加代码标志中间。

## 作业提交内容

- 完善后的程序代码
- 书面报告

## 作业相关文件

- [Python 代码](/teaching/PRML/PRML_Logistic_Regression.py)
- [数据文件1](/teaching/PRML/Logistic_data1.txt)
- [数据文件2](/teaching/PRML/Logistic_data2.txt)

## 作业中需要实现的函数

- `plot_data` 绘制二维的分类数据。
- `sigmoid` Sigmoid函数
- `cost_function` 逻辑回归的代价函数
- `predict` 逻辑回归的预测函数
- `cost_function_reg` 逻辑回归带正则化项的代价函数

# 逻辑回归

本次作业的目的是建立一个逻辑回归模型，用于预测一个学生是否应该被大学录取。

简单起见，大学通过两次考试的成绩来确定一个学生是否应该录取。你有以前数届考生的成绩，可以做为训练集学习逻辑回归模型。每个训练样本包括了考生两次考试的成绩和对应的录取决定。

你的任务是建立一个分类模型，根据两次考试的成绩来估计考生被录取的概率。

## 数据可视化

在实现机器学习算法前，可视化的显示数据以观察其规律通常是有益的。本次作业中，你需要实现 `plot_data` 函数，用于绘制所给数据的散点图。你绘制的图像应如下图所示，两坐标轴分别为两次考试的成绩，正负样本分别使用不同的标记显示。

![image](/teaching/PRML/LR_data1_visual.png)

如果你熟悉绘图程序，可以尝试自己完成框架。下面的代码供你参考：

```python
pos = y == 1
neg = y == 0
plt.plot(X[pos, 0], X[pos, 1], 'r+', label="Admitted")
plt.plot(X[neg, 0], X[neg, 1], 'bo', label="Not admitted")
```

## 热身练习：Sigmoid 函数

逻辑回归的假设模型为
<div> \[h_{\theta}(\pmb{x}) = g(\pmb{\theta}^{\mathrm{T}} \pmb{x})\] </div>
其中函数 \\(g(\cdot)\\) 是Sigmoid函数，定义为
<div> \[g(z) = \frac{1}{1 + \exp(-z)}.\] </div>

本练习中第一步需要你实现 Sigmoid 函数。在实现该函数后，你需要确认其功能正确。对于输入为矩阵和向量的情况，你实现的函数应当对每一个元素执行Sigmoid 函数。

## 代价函数与梯度

现在你需要实现逻辑回归的代价函数及其梯度。补充完整 `cost_function` 函数，使其返回正确的代价。补充完整 `cost_gradient` 函数，使其返回正确的梯度。

逻辑回归的代价函数为
<div> \[J(\theta) = \frac{1}{m} \sum_{i=1}^{m} \Big[ -y^{(i)} \log \big( h_{\theta}(x^{(i)}) \big) - (1-y^{(i)}) \log \big( 1-h_{\theta}(x^{(i)}) \big) \Big]\] </div>
对应的梯度向量各分量为
<div> \[\frac{\partial J(\theta)}{\partial \theta_{j}} = \frac{1}{m} \sum_{i=1}^{m} \big( h_{\theta}(x^{(i)}) - y^{(i)} \big) x_{j}^{(i)}\] </div>

传入初始参数， `cost_function` 的代价约为 0.693。

## 使用 `scipy.optimize.fmin_cg` 学习模型参数

在本次作业中，希望你使用 `scipy.optimize.fmin_cg` 函数实现代价函数\\(J(\theta)\\)的优化，得到最佳参数\\(\theta^{*}\\)。

使用该优化函数的代码已经在程序中实现，调用方式示例如下：

```python
ret = op.fmin_cg(cost_function,
                 theta,
                 fprime=cost_gradient,
                 args=(X, y),
                 maxiter=400,
                 full_output=True)
theta_opt, cost_min, _, _, _ = ret
```

其中 `cost_function` 为代价函数， `theta` 为需要优化的参数初始值， `fprime=cost_gradient` 给出了代价函数的梯度， `args=(X, y)` 给出了需要优化的函 数与对应的梯度计算所需要的其他参数， `maxiter=400` 给出了最大迭代次数， `full_output=True` 则指明该函数除了输出优化得到的参数 `theta_opt` 外，还会返 回最小的代价函数值 `cost_min` 等内容。

对第一组参数，得到的代价约为 0.203 (`cost_min`)。

你可以调用 `plot_decision_boundary` 函数来查看最终得到的分类面。建议你认真阅读 `plot_decision_boundary` 的代码。

![image](/teaching/PRML/LR_data1_boundary.png)

## 评估逻辑回归模型

在获得模型参数后，你就可以使用模型预测一个学生能够被大学录取。如果某学生考试一的 成绩为45，考试二的成绩为85，你应该能够得到其录取概率约为0.776。

你需要完成 `predict` 函数，该函数输出“1”或“0”。通过计算分类正确的样本百分数， 我们可以得到训练集上的正确率。

# 正则化的逻辑回归

## 数据可视化

调用函数 `plot_data` 可视化第二组数据 `HW1602_data2.txt` 。

![image](/teaching/PRML/LR_data2_visual.png)

### 特征变换

创建更多的特征是充分挖掘数据中的信息的一种有效手段。在函数 `map_feature` 中，我们将数据映射为其六阶多项式的所有项。
<div>
  \[\text{map_feature}(\pmb{x}) = \begin{bmatrix} 1\\ x_1\\ x_2 \\ x_1^2 \\ x_1 x_2 \\
    x_2^2 \\ x_1^3 \\ \vdots \\ x_1 x_2^5 \\ x_2^6 \end{bmatrix} \]
</div>

## 代价函数与梯度

逻辑回归的代价函数为
<div> \[J(\theta) = \frac{1}{m} \sum_{i=1}^{m} \Big[ -y^{(i)} \log \big( h_{\theta}(x^{(i)}) \big) - (1-y^{(i)}) \log \big( 1-h_{\theta}(x^{(i)}) \big) \Big] + \frac{\lambda}{2m} \sum_{j=1}^{n} \theta_{j}^{2}\] </div>
对应的梯度向量各分量为
<div>
\[\begin{split}
\frac{\partial J(\theta)}{\partial \theta_{0}} &= \frac{1}{m} \sum_{i=1}^{m} \big( h_{\theta}(x^{(i)}) - y^{(i)} \big) x_{0}^{(i)} \qquad \qquad \text{for } j=0 \\
\frac{\partial J(\theta)}{\partial \theta_{j}} &= \frac{1}{m} \sum_{i=1}^{m} \big( h_{\theta}(x^{(i)}) - y^{(i)} \big) x_{j}^{(i)} + \frac{\lambda}{m} \theta_{j} \qquad \text{for } j \geq 1
\end{split}\]
</div>
如果将参数\\(\theta\\)初始化为全零值，相应的代价函数约为 0.693。可以使用与前述无正则化项类似的方法实现梯度下降，获得优化后的参数\\(\theta^{*}\\)。

你可以调用 `plot_decision_boundary` 函数来查看最终得到的分类面。建议你调整正则化项的系数，分析正则化对分类面的影响。

![image](/teaching/PRML/LR_data2_boundary.png)
