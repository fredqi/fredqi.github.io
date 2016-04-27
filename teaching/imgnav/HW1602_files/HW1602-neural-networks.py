# coding: utf-8

import numpy as np
import scipy.io as sio
from scipy.optimize import fmin_cg
import matplotlib.pyplot as plt


def display_data(data, img_width=20):
    """将图像数据 data 按照矩阵形式显示出来"""
    plt.figure()
    # 计算数据尺寸相关数据
    n_rows, n_cols = data.shape
    img_height = n_cols // img_width

    # 计算显示行数与列数
    disp_rows = int(np.sqrt(n_rows))
    disp_cols = (n_rows + disp_rows - 1) // disp_rows

    # 图像行与列之间的间隔
    pad = 1
    disp_array = np.ones((pad + disp_rows*(img_height + pad),
                          pad + disp_cols*(img_width + pad)))

    idx = 0
    for row in range(disp_rows):
        for col in range(disp_cols):
            pass  # Remove this line
    # ====================== YOUR CODE HERE ======================

    # ===================== END OF YOUR CODE =====================

    plt.imshow(disp_array)

    plt.gray()
    plt.axis('off')
    plt.show()


def nn_cost_function(nn_params, *args):
    """Cost function of neural network.

    :param nn_params: parameters (weights) of the neural netwrok.
                      It is a 1D array including weights of all layers.
    :returns: J, the cost of the neural network.
    :rtype: float

    """
    # Unpack parameters from *args
    input_layer_size, hidden_layer_size, num_labels, lmb, X, y = args
    # Unroll weights of neural networks from nn_params
    Theta1 = nn_params[:hidden_layer_size*(input_layer_size + 1)]
    Theta1 = Theta1.reshape((hidden_layer_size, input_layer_size + 1))
    Theta2 = nn_params[hidden_layer_size*(input_layer_size + 1):]
    Theta2 = Theta2.reshape((num_labels, hidden_layer_size + 1))

    # Setup some useful variables
    m = X.shape[0]

    # You need to return the following variable correctly
    J = 0.0

    # ====================== YOUR CODE HERE ======================

    # Regularization Term

    # ===================== END OF YOUR CODE =====================
    return J


def nn_grad_function(nn_params, *args):
    """Gradient of the cost function of neural network.

    :param nn_params: parameters (weights) of the neural netwrok.
                      It is a 1D array including weights of all layers.
    :returns: grad, the gradient of the cost of the neural network.
    :rtype: float

    """
    # Unpack parameters from *args
    input_layer_size, hidden_layer_size, num_labels, lmb, X, y = args
    # Unroll weights of neural networks from nn_params
    Theta1 = nn_params[:hidden_layer_size*(input_layer_size + 1)]
    Theta1 = Theta1.reshape((hidden_layer_size, input_layer_size + 1))
    Theta2 = nn_params[hidden_layer_size*(input_layer_size + 1):]
    Theta2 = Theta2.reshape((num_labels, hidden_layer_size + 1))

    # Setup some useful variables
    m = X.shape[0]
    # You need to setup the following variables correctly
    Theta1_grad = np.zeros_like(Theta1)
    Theta2_grad = np.zeros_like(Theta2)
    # ====================== YOUR CODE HERE ======================
    # You may need to perform feedforward pass again as in
    # nn_cost_function

    # Regularization Term

    # ===================== END OF YOUR CODE =====================
    # Unroll gradients
    grad = np.hstack((Theta1_grad.flatten(), Theta2_grad.flatten()))
    return grad


def sigmoid(z):
    """Sigmoid function"""
    z = np.asarray(z)
    s = np.zeros_like(z)
    # ====================== YOUR CODE HERE ======================

    # ===================== END OF YOUR CODE =====================
    return s


def sigmoid_gradient(z):
    """Gradient of sigmoid function."""
    g = np.zeros_like(z)
    # ====================== YOUR CODE HERE ======================

    # ===================== END OF YOUR CODE =====================
    return g


def rand_initialize_weigths(L_in, L_out):
    """Randomly initialize the weights of a layer with L_in incoming
    connections and L_out outgoing connections"""

    # You need to return the following variables correctly
    W = np.zeros((L_out, 1 + L_in))
    # ====================== YOUR CODE HERE ======================

    # ===================== END OF YOUR CODE =====================
    return W


def predict(Theta1, Theta2, X):
    """Make prediction."""
    # Useful values
    m = X.shape[0]
    # num_labels = Theta2.shape[0]

    # You need to return the following variables correctly
    p = np.zeros((m,1), dtype=int)
    # ====================== YOUR CODE HERE ======================

    # ===================== END OF YOUR CODE =====================
    # print h1.shape, h2.shape
    p = np.argmax(h2, axis=1) + 1.0
    return p


def compute_numerical_gradient(cost_func, theta):
    """Compute the numerical gradient of the given cost_func
    at parameter theta"""

    numgrad = np.zeros_like(theta)
    perturb = np.zeros_like(theta)
    eps = 1.0e-4
    for idx in range(len(theta)):
        perturb[idx] = eps
        loss1 = cost_func(theta - perturb)
        loss2 = cost_func(theta + perturb)
        numgrad[idx] = (loss2 - loss1)/(2*eps)
        perturb[idx] = 0.0
    return numgrad


def debug_initialize_weights(fan_out, fan_in):
    """Initalize the weights of a layer with
    fan_in incoming connections and
    fan_out outgoing connection using a fixed strategy."""

    W = np.linspace(1, fan_out*(fan_in+1), fan_out*(fan_in+1))
    W = 0.1*np.sin(W).reshape(fan_out, fan_in + 1)
    return W


def check_nn_gradients(lmb=0.0):
    """Creates a small neural network to check the backgropagation
    gradients."""
    input_layer_size, hidden_layer_size = 3, 5
    num_labels, m = 3, 5

    Theta1 = debug_initialize_weights(hidden_layer_size, input_layer_size)
    Theta2 = debug_initialize_weights(num_labels, hidden_layer_size)

    X = debug_initialize_weights(m, input_layer_size - 1)
    y = np.array([1 + (t % num_labels) for t in range(m)])
    nn_params = np.hstack((Theta1.flatten(), Theta2.flatten()))

    cost_func = lambda x: nn_cost_function(x,
                                           input_layer_size,
                                           hidden_layer_size,
                                           num_labels, lmb, X, y)
    grad = nn_grad_function(nn_params,
                            input_layer_size, hidden_layer_size,
                            num_labels, lmb, X, y)
    numgrad = compute_numerical_gradient(cost_func, nn_params)
    print np.vstack((numgrad, grad)).T, np.sum(np.abs(numgrad - grad))
    print 'The above two columns you get should be very similar.'
    print '(Left-Your Numerical Gradient, Right-Analytical Gradient)'


if __name__ == '__main__':
    
    # Parameters
    input_layer_size = 400          # 20x20 大小的输入图像，图像内容为手写数字
    hidden_layer_size = 25          # 25 hidden units
    num_labels = 10                 # 10 类标号 从1到10

    # =========== 第一部分 ===============
    # 加载训练数据
    print "Loading and Visualizing Data..."
    data = sio.loadmat('HW1602data.mat')
    X, y = data['X'], data['y']

    m = X.shape[0]

    # 随机选取100个数据显示
    rand_indices = range(m)
    np.random.shuffle(rand_indices)
    X_sel = X[rand_indices[:100]]

    display_data(X_sel)

    # =========== 第二部分 ===============
    print 'Loading Saved Neural Network Parameters ...'

    # Load the weights into variables Theta1 and Theta2
    # Theta1 has size 25 x 401
    # Theta2 has size 10 x 26
    data = sio.loadmat('HW1602weights.mat')
    Theta1, Theta2 = data['Theta1'], data['Theta2']

    # print Theta1.shape, (hidden_layer_size, input_layer_size + 1)
    # print Theta2.shape, (num_labels, hidden_layer_size + 1)

    # ================ Part 3: Compute Cost (Feedforward) ================

    #  To the neural network, you should first start by implementing the
    #  feedforward part of the neural network that returns the cost only. You
    #  should complete the code in nnCostFunction.m to return cost. After
    #  implementing the feedforward to compute the cost, you can verify that
    #  your implementation is correct by verifying that you get the same cost
    #  as us for the fixed debugging parameters.
    #
    #  We suggest implementing the feedforward cost *without* regularization
    #  first so that it will be easier for you to debug. Later, in part 4, you
    #  will get to implement the regularized cost.

    print 'Feedforward Using Neural Network ...'

    # Weight regularization parameter (we set this to 0 here).
    lmb = 0.0

    nn_params = np.hstack((Theta1.flatten(), Theta2.flatten()))
    J = nn_cost_function(nn_params,
                         input_layer_size, hidden_layer_size,
                         num_labels, lmb, X, y)

    print 'Cost at parameters (loaded from ex4weights): %f ' % J
    print '(this value should be about 0.287629)'

    # =============== Part 4: Implement Regularization ===============
    print 'Checking Cost Function (w/ Regularization) ... '
    lmb = 1.0

    J = nn_cost_function(nn_params,
                         input_layer_size, hidden_layer_size,
                         num_labels, lmb, X, y)

    print 'Cost at parameters (loaded from ex4weights): %f ' % J
    print '(this value should be about 0.383770)'


    # ================ Part 5: Sigmoid Gradient  ================
    print 'Evaluating sigmoid gradient...'

    g = sigmoid_gradient([1, -0.5, 0, 0.5, 1])
    print 'Sigmoid gradient evaluated at [1 -0.5 0 0.5 1]:  '
    print g


    #  ================ Part 6: Initializing Pameters ================
    print 'Initializing Neural Network Parameters ...'
    initial_Theta1 = rand_initialize_weigths(input_layer_size, hidden_layer_size)
    initial_Theta2 = rand_initialize_weigths(hidden_layer_size, num_labels)

    # Unroll parameters
    initial_nn_params = np.hstack((initial_Theta1.flatten(),
                                   initial_Theta2.flatten()))

    # =============== Part 7: Implement Backpropagation ===============
    print 'Checking Backpropagation... '

    # Check gradients by running checkNNGradients
    check_nn_gradients()

    # =============== Part 8: Implement Regularization ===============
    print 'Checking Backpropagation (w/ Regularization) ... '
    #  Check gradients by running checkNNGradients
    lmb = 3.0
    check_nn_gradients(lmb)

    # =================== Part 8: Training NN ===================
    print 'Training Neural Network...'

    lmb, maxiter = 1.0, 40
    args = (input_layer_size, hidden_layer_size, num_labels, lmb, X, y)
    nn_params, cost_min, _, _, _ = fmin_cg(nn_cost_function,
                                           initial_nn_params,
                                           fprime=nn_grad_function,
                                           args=args,
                                           maxiter=maxiter,
                                           full_output=True)

    Theta1 = nn_params[:hidden_layer_size*(input_layer_size + 1)]
    Theta1 = Theta1.reshape((hidden_layer_size, input_layer_size + 1))
    Theta2 = nn_params[hidden_layer_size*(input_layer_size + 1):]
    Theta2 = Theta2.reshape((num_labels, hidden_layer_size + 1))

    # ================= Part 9: Visualize Weights =================
    print 'Visualizing Neural Network... '
    display_data(Theta1[:, 1:])

    # ================= Part 10: Implement Predict =================

    pred = predict(Theta1, Theta2, X)
    print 'Training Set Accuracy:', np.mean(pred == y[:, 0])*100.0
