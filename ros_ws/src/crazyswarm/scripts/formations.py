#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

from pycrazyswarm import *
from scipy.spatial import distance

def pos_from_circle(num_agents, radius, center=(0., 0.), Z=1.5):
    pts = []
    x0, y0 = center
    for i in range(num_agents):
        x_i = x0 + radius * np.cos(2 * np.pi * i / num_agents)
        y_i = y0 + radius * np.sin(2 * np.pi * i / num_agents)
        pts.append(np.array([x_i, y_i, Z]))

    return pts


if __name__ == '__main__':
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf_array = allcfs.crazyflies

    Z = 1.5
    ids = [3, 17, 20, 27, 28, 33, 41, 47]
    cfs = [allcfs.crazyfliesById[i] for i in ids]
    init_poses = [np.array(cf.position()) + np.array([0., 0., Z]) for cf in cfs]

    print("Taking off...\n")
    allcfs.takeoff(targetHeight=Z, duration=3.0)
    timeHelper.sleep(6.0)

    # circular formation in the x-y plane
    pts = pos_from_circle(num_agents=8, radius=1.5)
    for cf, pt in zip(cfs, pts):
        cf.goTo(goal=pt, yaw=0, duration=3.0)
    timeHelper.sleep(6.0)

    print("Returning...\n")
    for cf, init_pos in zip(cfs, init_poses):
        cf.goTo(init_pos, yaw=0, duration=3.0)
    timeHelper.sleep(5.0)

    print("Landing...\n")
    allcfs.land(targetHeight=0.04, duration=4.0)
    timeHelper.sleep(4.0)


