import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    res = np.array(x > 0, dtype=np.int)
    print (np.int)
    print (res)
    return res

if __name__ == '__main__':
    x = np.arange(-5.0, 5.0, 0.1)  # -5.0 -4.9 ... 4.9 5.0
    y = step_function(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()
