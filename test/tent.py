import numpy as np
import matplotlib.pyplot as plt


def f( arr ):
    y_sqrt = (25 - (arr - 5) ** 2) ** 0.5
    y_sqrt[len(y_sqrt // 2):] *= -1
    temp = y_sqrt[len(y_sqrt // 2):] * -1
    print(temp)
    y_sqrt2 = np.concatenate([y_sqrt[:len(y_sqrt // 2)], y_sqrt[len(y_sqrt // 2):] * -1])
    print(y_sqrt2)
    y_t = np.block([y_sqrt[:(len(arr) // 2)], (y_sqrt[(len(arr) // 2):] * -1 - 5) * -1])
    return y_sqrt2


size = 10
x = np.random.random_sample(size, ) * 10
y = f(x)
plt.scatter(x, y)
plt.show()
