import numpy as np
import matplotlib.pyplot as plt


def f( arr ):
    y_sqrt = np.random.random_sample(size, ) * (25 - (arr - 5) ** 2) ** 0.5
    y_t = np.block([y_sqrt[:(len(arr) // 2)], (y_sqrt[(len(arr) // 2):] * -1)])
    return y_t


def sampling( arr_x, arr_y, rate ):
    rdm = np.random.randint(0, len(arr_x), (len(arr_x) // rate,))
    return arr_x[rdm], arr_y[rdm]


size = 100000

fig = plt.figure()
plt.subplots_adjust(wspace=0.5, hspace=0.5)

ax_1 = fig.add_subplot(2, 2, 1)
ax_1.set_aspect(1.0 / ax_1.get_data_ratio(), adjustable='box')
ax_1.set_title(f"size:{size}")
x = np.random.random_sample(size, ) * 10
y = f(x)
plt.scatter(x, y, s=1)

ax_2 = fig.add_subplot(2, 2, 2)
ax_2.set_aspect(1.0 / ax_2.get_data_ratio(), adjustable='box')
ax_2.set_title(f"size:{size // 10}")
x2, y2 = sampling(x, y, 10)
plt.scatter(x2, y2, s=1)

ax_3 = fig.add_subplot(2, 2, 3)
ax_3.set_aspect(1.0 / ax_3.get_data_ratio(), adjustable='box')
ax_3.set_title(f"size:{size // 50}")
x3, y3 = sampling(x, y, 50)
plt.scatter(x3, y3, s=1)

ax_4 = fig.add_subplot(2, 2, 4)
ax_4.set_aspect(1.0 / ax_4.get_data_ratio(), adjustable='box')
ax_4.set_title(f"size:{size // 100}")
x4, y4 = sampling(x, y, 100)
plt.scatter(x4, y4, s=1)

plt.show()
