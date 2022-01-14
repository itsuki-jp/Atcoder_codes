import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation

fig, ax = plt.subplots()

arr = np.array([[1, 0.1], [0.1, 1]])
xy = []
step = 0.01
for i in np.arange(-1, 1 + step, step):
    for j in np.arange(-1, 1 + step, step):
        xy.append([i, j])

artists = []
for i in range(10):
    x = [i[0] for i in xy]
    y = [i[1] for i in xy]
    artists.append(ax.plot(x, y, "blue"))
    xy = [np.dot(arr, i) for i in xy]

anim = ArtistAnimation(fig, artists, interval=1000)
plt.show()
anim.save("output.gif", writer="pillow")
