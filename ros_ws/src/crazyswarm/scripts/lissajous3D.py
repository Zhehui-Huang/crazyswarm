#!/usr/bin/env python
import numpy as np
from pycrazyswarm import *

def lissajous3D(tick, a=1.8, b=1.0, c=0.2, n=2, m=2, phi=0, psi=np.pi):
    x = a * np.sin(tick)
    y = b * np.sin(n * tick + phi)
    z = c * np.cos(m * tick + psi)
    return x, y, z

def get_new_goal(iter=0, prev_goal=np.array([0., 0., 2.])):
    x, y, z = lissajous3D(iter)
    print(x, y, z)
    goal_x, goal_y, goal_z = prev_goal
    x_new, y_new, z_new = x + goal_x, y + goal_y, z + goal_z
    new_goal = np.array([x_new, y_new, z_new])
    return new_goal

if __name__  == '__main__':
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf_array = allcfs.crazyflies
    # ids = [3, 17, 20, 27, 28, 33, 41, 47]
    ids = [3, 17, 41, 47]
    cfs = [allcfs.crazyfliesById[id] for id in ids]

    Z = 2.0
    init_poses = [np.array(cf.position()) + np.array([0., 0., Z]) for cf in cfs]

    print("Taking off... \n")
    allcfs.takeoff(targetHeight=Z, duration=3.0)
    timeHelper.sleep(4.0)

    print("pursuing...\n")
    goal = np.array([0, 0, 2])
    points = []

    for t in np.arange(0, 4 * np.pi, 0.10):
        # goal = get_new_goal(iter=t, prev_goal=goal, steps=steps)
        x,y,z = lissajous3D(t)
        goal = np.array([x, y, z])
        # tmp_x, tmp_y, tmp_z = goal
        # new_x = tmp_x
        # new_y = tmp_y
        # new_z = tmp_z
        # goal = np.array([new_x, new_y, new_z])
        points.append(goal)

    points = np.concatenate(points, axis=0).reshape(-1, 3) + (0., 0., 2.0)
    print("Seconds of flight: ", len(points) * 0.1)
    for goal in points:
        print(goal)
        for cf in cfs:
            cf.cmdPosition(pos=goal, yaw=0)
        timeHelper.sleep(0.1)

    print("Returning to init poses")
    for _ in range(40):
        for cf, pos in zip(cfs, init_poses):
            cf.cmdPosition(pos=pos, yaw=0)
        timeHelper.sleep(0.1)
    timeHelper.sleep(2.0)

    print("landing")
    # manually land over 3 seconds
    for _ in range(30):
        for i, cfid in enumerate(ids):
            curPos = init_poses[i]
            curPos -= np.array([0., 0., 0.03])
            allcfs.crazyfliesById[cfid].cmdPosition(curPos)
        timeHelper.sleep(0.1)