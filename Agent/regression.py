import numpy as np
import matplotlib.pyplot as plt
from sympy import *

#residual = (y - (ax + b))^2

def linear_regression(x, y):
    a, b = symbols('a b')
    residual = 0
    num = len(x)
    
    for i in range(num):
        residual += (y[i] - (a * x[i] + b)) ** 2
    #print expand(residual)

    #differential to a & b
    f1 = diff(residual, a)
    f2 = diff(residual, b)

    #solve two equations
    res = solve([f1, f2], [a, b])
    return res[a], res[b]
    
def main():
    
    X = np.linspace(0, 10)
    f = lambda x: x
    F = np.vectorize(f)

    n = 20
    random_sign = np.vectorize(lambda x: x if np.random.sample() > 0.5 else -x)
    data_X = np.linspace(1, 9, n)
    data_Y = random_sign(np.random.sample(n) * 2) + F(data_X)

    print data_X
    print data_Y
    
    a, b = linear_regression(data_X, data_Y)
    f = lambda x: a * x + b
    Fvec = np.vectorize(f)
    regression_y = Fvec(data_X)

    plt.plot(data_X, regression_y, 'g')
    plt.plot(data_X, data_Y, 'ro')
    
    plt.show()
    
    
if __name__ == "__main__":
    main()
