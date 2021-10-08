#!/usr/bin/env python

import numpy as np

from pycrazyswarm import *

if __name__ == '__main__':
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf_array = allcfs.crazyflies

    z = 1.5
    ids = [3, 20, 41, 47]
    cfs = [allcfs.crazyfliesById[i] for i in ids]

    init_pos = {20: np.array([1., -1., z]),
                47: np.array([-1., -1., z]),
                3: np.array([1.0, 1.0, z]),
                41: np.array([-1., 1., z])}

    print("Taking off... \n")
    allcfs.takeoff(targetHeight=z, duration=3.0)
    timeHelper.sleep(4.0)


    print("Moving to goal..\n")
    # for _ in range(70):
    #     # allcfs.crazyfliesById[20].cmdPosition(pos=init_pos[47])
    #     # allcfs.crazyfliesById[47].cmdPosition(pos=init_pos[20])
    #     allcfs.crazyfliesById[3].cmdPosition(pos=init_pos[41])
    #     allcfs.crazyfliesById[41].cmdPosition(pos=init_pos[3])
    #     timeHelper.sleep(0.1)
    allcfs.crazyfliesById[3].goTo(goal=init_pos[41], yaw=0, duration=4.0)
    allcfs.crazyfliesById[41].goTo(goal=init_pos[3], yaw=0, duration=4.0)

    allcfs.crazyfliesById[20].goTo(goal=init_pos[47], yaw=0, duration=4.0)
    allcfs.crazyfliesById[47].goTo(goal=init_pos[20], yaw=0, duration=4.0)

    timeHelper.sleep(7.0)


    print("Returning...\n")
    # for _ in range(60):
    #     for cfid in ids:
    #         allcfs.crazyfliesById[cfid].cmdPosition(pos=init_pos[cfid])
    #     timeHelper.sleep(0.1)
    for cfid in ids:
        allcfs.crazyfliesById[cfid].goTo(goal=init_pos[cfid], yaw=0, duration=4.0)
    timeHelper.sleep(6.0)

    print("landing\n")
    allcfs.land(0.04, duration=4.0)
    timeHelper.sleep(3.0)


