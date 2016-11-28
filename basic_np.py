import numpy as np

if __name__ == '__main__':

    a = np.array([1, 2, 3])
    print ("=> a")
    print (a)

    b = np.array([[1.5, 0], [0, 3.0]])
    print ("=> b")
    print (b)

    c = np.ones((2, 3))
    print ("=> c")
    print (c)

    d = np.array(1 > 0)
    print ("=> d")
    print (d)

    e = np.array(1 > 0, dtype=np.int)
    print ("=> e")
    print (e)

    f = np.exp(0)
    print ("=> f")
    print (f)

    g = np.exp(1)
    print ("=> g")
    print (g)

    h = np.exp(-1)
    print ("=> h")
    print (h)

    i = np.exp(-2)
    print ("=> i")
    print (i)
