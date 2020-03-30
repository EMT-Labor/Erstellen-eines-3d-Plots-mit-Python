import mpl_toolkits 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-7, 7, 30)
y = np.linspace(-7, 7, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)