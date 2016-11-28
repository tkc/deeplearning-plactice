import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    res = 1 / (1 + np.exp(-x))
    print  (np.exp(-x))
    print  (res)
    return res

if __name__ == '__main__':
    x = np.arange(-5.0, 5.0, 0.1)  # -5.0 -4.9 ... 4.9 5.0
    y = sigmoid(x)
    print  (x)
    print  (y)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()
