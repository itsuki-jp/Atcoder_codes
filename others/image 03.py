import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()

print(pd.DataFrame(iris.data,columns=iris.feature_names))