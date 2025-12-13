import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure(figsize=(1200,1200))
ax = plt.axes(projection="3d")
start = 0
stop = 2 * math.pi
num_points = 1000
time_linespace = np.linspace(start, stop, num_points)
i_vector = time_linespace - np.sin(time_linespace)
j_vector = 1 - np.cos(time_linespace)
ax.plot3D(i_vector, j_vector, time_linespace)
plt.show()