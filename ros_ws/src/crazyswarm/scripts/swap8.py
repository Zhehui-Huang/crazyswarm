#!/usr/bin/env python

import numpy as np
from pycrazyswarm import *

if __name__ == '__main__':
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    ids = [7, 10, 11, 12, 14, 20, 21, 45]
    init_pos = {7: np.array([0.0, 3.0, 2.5]),
                10: np.array([0.0, 2.0, 2.5]),
                11: np.array([-2.0, 3.0, 2.5]),
                12: np.array([-2.0, 2.0, 2.5]),
                14: np.array([0.0, -3.0, 2.5]),
                20: np.array([0.0, -2.0, 2.5]),
                21: np.array([-2.0, -3.0, 2.5]),
                45: np.array([-2.0, -2.0, 2.5])}

    # swap in the y-dir

    cfs = [allcfs.crazyfliesById[i] for i in ids]

    print("taking off..\n")
    allcfs.takeoff(targetHeight=2.5, duration=2.5)
    timeHelper.sleep(5.0)

    print('swapping once')
    allcfs.crazyfliesById[7].goTo(init_pos[20], yaw=0.0, duration=5.0)
    allcfs.crazyfliesById[10].goTo(init_pos[14], yaw=0.0, duration=5.0)
    allcfs.crazyfliesById[11].goTo(init_pos[45], yaw=0.0, duration=5.0)
    allcfs.crazyfliesById[12].goTo(init_pos[21], yaw=0.0, duration=5.0)

    allcfs.crazyfliesById[20].goTo(init_pos[7], yaw=0.0, duration=5.0)
    allcfs.crazyfliesById[14].goTo(init_pos[10], yaw=0.0, duration=5.0)
    allcfs.crazyfliesById[45].goTo(init_pos[11], yaw=0.0, duration=5.0)
    allcfs.crazyfliesById[21].goTo(init_pos[12], yaw=0.0, duration=5.0)

    timeHelper.sleep(5.0)

    print("returning..")
    for cfid in ids:
        allcfs.crazyfliesById[cfid].goTo(init_pos[cfid], yaw=0.0, duration=5.0)
    timeHelper.sleep(5.0)

    print("landing")
    allcfs.land(0.0, duration=4.0)
    timeHelper.sleep(4.0)