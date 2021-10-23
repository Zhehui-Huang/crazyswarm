#!/usr/bin/env python

import numpy as np

from pycrazyswarm import *

if __name__ == '__main__':
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf_array = allcfs.crazyflies

    Z = 1.5
    # ids = [3, 17, 20, 27, 28, 33, 41, 47]
    ids = [3, 28]
    team1 = [allcfs.crazyfliesById[i] for i in ids[:len(ids)/2]]
    team2 = [allcfs.crazyfliesById[i] for i in ids[len(ids)/2:]]

    init_poses1 = [np.array(cf.position()) + np.array([0., 0., Z]) for cf in team1]
    init_poses2 = [np.array(cf.position()) + np.array([0., 0., Z]) for cf in team2]

    print("Taking off...\n")
    allcfs.takeoff(targetHeight=Z, duration=3.0)
    timeHelper.sleep(3.0)

    print("Swapping...\n")
    for cf1, cf2, init_pos1, init_pos2 in zip(team1, team2, init_poses1, init_poses2):
        cf1.goTo(goal=init_pos2, yaw=0, duration=4.0)
        cf2.goTo(goal=init_pos1, yaw=0, duration=4.0)
    timeHelper.sleep(6.0)

    print("Swapping back...\n")
    for cf1, cf2, init_pos1, init_pos2 in zip(team1, team2, init_poses1, init_poses2):
        cf1.goTo(goal=init_pos1, yaw=0, duration=4.0)
        cf2.goTo(goal=init_pos2, yaw=0, duration=4.0)
    timeHelper.sleep(6.0)

    print('landing\n')
    allcfs.land(0.04, duration=4.0)
    timeHelper.sleep(3.0)
