import numpy as np
import pyviz3d as viz

points = np.array([[2.0, 0.0, 0.0],
                   [0.0, 2.0, 0.0],
                   [0.0, 0.0, 2.0]])

colors = np.array([[255, 0, 0],
                   [0, 255, 0],
                   [0, 0, 255]])

viz.show_pointclouds([points], [colors], point_size=30)
viz.show_pointclouds([points * 0.5], [colors], point_size=10)
