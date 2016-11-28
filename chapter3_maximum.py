import numpy as np
import matplotlib.pylab as plt


def relu(x):
    return np.maximum(0, x)

if __name__ == '__main__':
    x = np.arange(-3.0, 3.0, 0.5)
    y = relu(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 3.1)
    plt.show()
