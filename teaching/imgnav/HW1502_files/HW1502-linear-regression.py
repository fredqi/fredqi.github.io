# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt


def warm_up_exercise():
    """热身练习"""
    A = None
    # ====================== 你的代码 ==========================
    # 在下面加入你的代码，使程序返回一个 5x5 的单位矩阵

    # =========================================================
    return A


def plot_data(x, y):
    """绘制给定数据x与y的图像"""
    plt.figure()
    # ====================== 你的代码 ==========================
    # 绘制x与y的图像
    # 使用 matplotlib.pyplt 的命令 plot, xlabel, ylabel 等。
    # 提示：可以使用 'rx' 选项使数据点显示为红色的 "x"，
    #       使用 "markersize=8, markeredgewidth=2" 使标记更大

    # 给制数据

    # 设置y轴标题为 'Profit in $10,000s'

    # 设置x轴标题为 'Population of City in 10,000s'

    # =========================================================
    plt.show()


def compute_cost(X, y, theta):
    """计算线性回归的代价。"""
    m = len(y)
    J = 0.0
    # ====================== 你的代码 ==========================
    # 计算给定 theta 参数下线性回归的代价
    # 请将正确的代价赋值给 J

    # =========================================================
    return J


def gradient_descent(X, y, theta, alpha, num_iters):
    """执行梯度下降算法来学习参数 theta。"""
    m = len(y)
    J_history = np.zeros((num_iters,))

    for iter in range(num_iters):
        # ====================== 你的代码 ==========================
        # 计算给定 theta 参数下线性回归的梯度，实现梯度下降算法

        # =========================================================
        # 将各次迭代后的代价进行记录
        J_history[iter] = compute_cost(X, y, theta)

    return theta, J_history


def plot_linear_fit(X, theta):
    """在绘制数据点的基础上绘制回归得到直线"""
    # ====================== 你的代码 ==========================
    # 绘制x与y的图像
    # 使用 matplotlib.pyplt 的命令 plot, xlabel, ylabel 等。
    # 提示：可以使用 'rx' 选项使数据点显示为红色的 "x"，
    #      使用 "markersize=8, markeredgewidth=2" 使标记更大
    #      使用"label=<your label>"设置数据标识，
    #      如 "label='Data'" 表示原始数据点
    #      "label='Linear Regression'" 表示线性回归的结果

    # 给制数据

    # 使用 legned 命令显示图例，图例显示位置为 "loc='lower right'"

    # 设置y轴标题为 'Profit in $10,000s'

    # 设置x轴标题为 'Population of City in 10,000s'

    # =========================================================
    plt.show()


def plot_visualize_cost(X, y, theta_best):
    """可视化代价函数"""

    # 生成参数网格
    theta0_vals = np.linspace(-10, 10, 101)
    theta1_vals = np.linspace(-1, 4, 101)
    t = np.zeros((2, 1))
    J_vals = np.zeros((101, 101))
    for i in range(101):
        for j in range(101):
            # =============== 你的代码 ===================
            # 加入代码，计算 J_vals 的值

            pass                # 完成你的代码后请删除此行
            # ===========================================

    plt.figure()
    plt.contour(theta0_vals, theta1_vals, J_vals,
                levels=np.logspace(-2, 3, 21))
    plt.plot(theta_best[0], theta_best[1], 'rx',
             markersize=8, markeredgewidth=2)
    plt.xlabel(r'$\theta_0$')
    plt.ylabel(r'$\theta_1$')
    plt.title(r'$J(\theta)$')
    plt.show()


if __name__ == '__main__':
    print('Running warm-up exercise ... \n')
    print('5x5 Identity Matrix: \n')
    A = warm_up_exercise()
    print(A)

    print('Plotting Data ...\n')
    data = np.loadtxt('HW1502-data.txt', delimiter=',')
    x, y = data[:, 0], data[:, 1]
    m = len(y)
    plot_data(x, y)
    plt.show()

    print('Running Gradient Descent ...\n')

    # Add a column of ones to x
    X = np.ones((m, 2))
    X[:, 1] = data[:, 0]

    # initialize fitting parameters
    theta = np.zeros((2, 1))

    # Some gradient descent settings
    iterations = 1500
    alpha = 0.01

    # compute and display initial cost
    # Expected value 32.07
    J0 = compute_cost(X, y, theta)
    print J0

    # run gradient descent
    # Expected value: theta = [-3.630291, 1.166362]
    theta, J_history = gradient_descent(X, y, theta,
                                        alpha, iterations)
    print('Theta found by gradient descent:')
    print('%f %f' % (theta[0], theta[1]))
    plot_linear_fit(X, theta)
    plt.show()

    plot_visualize_cost(X, y, theta)
    plt.show()
