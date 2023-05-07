#!/usr/bin/env python

import numpy as np

from pycrazyswarm import *

if __name__ == '__main__':
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf_array = allcfs.crazyflies

    z = 1.0
    ids = [2]
    cfs = [allcfs.crazyfliesById[i] for i in ids]

    # init_pos = {33: np.array([0., 1., z]),
    #             28: np.array([0., -1., z]),
    #             3: np.array([-1.0, 1.0, z]),
    #             47: np.array([-1.0, -1.0, z])}
    init_pos = [np.array(cf.position()) + np.array([0., 0., z]) for cf in cfs]

    print("Taking off... \n")
    allcfs.takeoff(targetHeight=z, duration=3.0)
    timeHelper.sleep(4.0)

    print("Moving to shared goal...\n")
    for cf in cfs:
        cf.goTo(goal=np.array([1., 0., z]), yaw=0.0, duration=3.0)
        timeHelper.sleep(3.0)
    timeHelper.sleep(7.0)

    print("Returning...\n")
    # for _ in range(60):
    #     for cfid in ids:
    #         allcfs.crazyfliesById[cfid].cmdPosition(pos=init_pos[cfid])
    #     timeHelper.sleep(0.1)
    for cf, pos in zip(cfs, init_pos):
        cf.goTo(goal=pos, yaw=0, duration=4.0)
    timeHelper.sleep(6.0)

    print("landing\n")
    allcfs.land(0.04, duration=4.0)
    timeHelper.sleep(3.0)