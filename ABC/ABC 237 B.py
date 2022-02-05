import numpy as np
import pandas as pd

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

arr_t = np.array(a).T
for _ in arr_t:
    print(*_)