import numpy as np

if __name__ == '__main__':
    a1 = np.array([1, 2, 3, 4])
    print (a1)
    print (np.ndim(a1))
    c1 = a1.shape
    print (a1.shape)
    print (a1.shape[0])

    a2 = np.array([[1, 2], [3, 4]])
    print (a2)
    print (np.ndim(a2))
    print (a2.shape)
    print (a2.shape[0])

    a3 = np.array([[1, 2], [3, 4]])
    b3 = np.array([[5, 6], [7, 8]])

    # 1*5+2*7 3*5+4*7
    # 1*6+2*8 3*6+4*8
    print (np.dot(a3, b3))

    a4 = np.array([[1, 2, 3], [4, 5, 6]])
    b4 = np.array([[1, 2], [3, 4], [5, 6]])
    print (np.dot(a4, b4))


