import numpy as np
import pandas as pd
import sklearn
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
import pyrenn as prn


def main():
    rnn_func()
    # input data set
    # x = np.array([[0, 0, 1],
    #               [0, 1, 1],
    #               [1, 0, 1],
    #               [1, 1, 1]])
    #
    # # output data set
    # y = np.array([[0, 0, 1, 1]]).T
    #
    # # seed random numbers to make calculation
    # # deterministic (just a good practice)
    # np.random.seed(1)
    #
    # # initialize weights randomly with mean 0
    # syn0 = 2 * np.random.random((3, 1)) - 1
    #
    # for iter in range(10000):
    #     # forward propagation
    #     l0 = x
    #     l1 = nonlin(np.dot(l0, syn0))
    #
    #     # how much did we miss?
    #     l1_error = y - l1
    #
    #     # multiply how much we missed by the
    #     # slope of the sigmoid at the values in l1
    #     l1_delta = l1_error * nonlin(l1, True)
    #
    #     # update weights
    #     syn0 += np.dot(l0.T, l1_delta)
    #
    # print("Output After Training:")
    # print(l1)


def random_plot():
    # Generate a data set and plot it

    np.random.seed(0)
    x, y = sklearn.datasets.make_moons(200, noise=0.20)
    plt.show(plt.scatter(x[:, 0], x[:, 1], s=40, c=y, cmap=plt.cm.Spectral))

    plt.savefig("temp.png")


# sigmoid function
def nonlin(x, deriv=False):
    if deriv is True:
        return x*(1-x)
    return 1/(1+np.exp(-x))


def rnn_func():
    df = pd.ExcelFile('example_data.xlsx').parse('friction')
    P = df.loc[0:40]['P']
    Y = df.loc[0:40]['Y']
    Ptest = df['Ptest'].values
    Ytest = df['Ytest'].values
    net = prn.CreateNN([1,3,3,1])
    net = prn.train_LM(P, Y, net, verbose=True, k_max=100, E_stop=1e-5)
    y = prn.NNOut(P, net)
    ytest = prn.NNOut(Ptest, net)
    fig = plt.figure(figsize=(11, 7))
    ax0 = fig.add_subplot(211)
    ax1 = fig.add_subplot(212)
    fs = 18

    # Train Data
    ax0.set_title('Train Data', fontsize=fs)
    ax0.plot(P, y, color='b', lw=2, label='NN Output')
    ax0.plot(P, Y, color='r', marker='None', linestyle=':', lw=3, markersize=8, label='Train Data')
    ax0.tick_params(labelsize=fs - 2)
    ax0.legend(fontsize=fs - 2, loc='upper left')
    ax0.grid()

    # Test Data
    ax1.set_title('Test Data', fontsize=fs)
    ax1.plot(Ptest, ytest, color='b', lw=2, label='NN Output')
    ax1.plot(Ptest, Ytest, color='r', marker='None', linestyle=':', lw=3, markersize=8, label='Test Data')
    ax1.tick_params(labelsize=fs - 2)
    ax1.legend(fontsize=fs - 2, loc='upper left')
    ax1.grid()

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
