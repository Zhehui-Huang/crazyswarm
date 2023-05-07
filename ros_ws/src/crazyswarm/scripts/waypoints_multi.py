#!/usr/bin/env python

import numpy as np
from pycrazyswarm import *

TAKE_OFF_DUR = 1.2
Z = 0.5
GOTO_DURATION = 0.2
if __name__ == '__main__':
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    ids = [1, 3]
    init_pos = {1: np.array([1.0, 1.0, 0.5]),
                3: np.array([-1.0, -1.0, 0.5]),
                }

    # swap in the y-dir

    cfs = [allcfs.crazyfliesById[i] for i in ids]
    cfs_pos = [[], []]

    print("taking off..\n")
    allcfs.takeoff(targetHeight=Z, duration=TAKE_OFF_DUR)
    timeHelper.sleep(TAKE_OFF_DUR + 0.2)
    cfs_pos[0].append(cfs[0].position())
    cfs_pos[1].append(cfs[1].position())

    z = Z
    for _ in range(10):
        z += 0.1
        allcfs.crazyfliesById[1].goTo([1., 1., z], yaw=0.0, duration=0.2)
        allcfs.crazyfliesById[3].goTo([-1., -1., z], yaw=0.0, duration=0.2)
        cfs_pos[0].append(cfs[0].position())
        cfs_pos[1].append(cfs[1].position())
        timeHelper.sleep(GOTO_DURATION + 0.1)

    cfs_pos[0].append(cfs[0].position())
    cfs_pos[1].append(cfs[1].position())
    timeHelper.sleep(2.0)
    allcfs.land(0.05, duration=4.0)
    timeHelper.sleep(6.0)
    # cfs_pos[0].append(cfs[0].position())
    # cfs_pos[1].append(cfs[1].position())
    print('pos 1:   ')
    for item in cfs_pos[0]:
        print(item)
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('pos 3:   ')
    for item in cfs_pos[1]:
        print(item)
