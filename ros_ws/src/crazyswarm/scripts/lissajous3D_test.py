#!/usr/bin/env python
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from pycrazyswarm import *

def lissajous3D(tick, a=1.5, b=1.0, c=0.2, n=2, m=2, phi=0, psi=np.pi):
    x = a * np.sin(tick)
    y = b * np.sin(n * tick + phi)
    z = c * np.cos(m * tick + psi)
    return x, y, z


def get_new_goal(iter=0, prev_goal=np.array([0., 0., 2.]), steps=16.0):
    x, y, z = lissajous3D(iter)
    print(x, y, z)
    goal_x, goal_y, goal_z = prev_goal
    x_new, y_new, z_new = x + goal_x, y + goal_y, z + goal_z
    new_goal = np.array([x_new, y_new, z_new])
    return new_goal

if __name__ == '__main__':
    goal = np.array([0, 0, 2])
    points = []

    steps = 10.0
    for t in np.arange(0, 4 * np.pi, 0.1):
        # goal = get_new_goal(iter=t, prev_goal=goal, steps=steps)
        x,y,z = lissajous3D(t)
        goal = np.array([x, y, z])
        # tmp_x, tmp_y, tmp_z = goal
        # new_x = tmp_x
        # new_y = tmp_y
        # new_z = tmp_z
        # goal = np.array([new_x, new_y, new_z])
        points.append(goal)
        print(goal)

    points = np.concatenate(points, axis=0).reshape(-1, 3) + (0, 0, 2.0)
    for point in points:
        print(point)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(points[:, 0], points[:, 1], points[:, 2])
    plt.show()