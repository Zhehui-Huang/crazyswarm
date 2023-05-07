#!/usr/bin/env python

import numpy as np

from pycrazyswarm import *

if __name__ == '__main__':
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf_array = allcfs.crazyflies

    Z = 0.5
    ids = [1,2,3,4]
    init_poses = {
        1: [1., -1., 0.],
        2: [1., 1., 0.],
        3: [-1., 1., 0.],
        4: [-1., -1., 0.]
    }
    offset = np.array([-2., 0., Z])

    while True:
        raw_input()
        print("Taking off...")
        allcfs.takeoff(targetHeight=Z, duration=3.0)
        timeHelper.sleep(4.0)

        print("Moving...")
        for id in ids:
            allcfs.crazyfliesById[id].goTo(goal=np.array(init_poses[id]) + offset, yaw=0, duration=3.0)
        timeHelper.sleep(10.0)

        print("Moving back...")
        for id in ids:
            allcfs.crazyfliesById[id].goTo(goal=np.array(init_poses[id]) + np.array([0., 0., Z]), yaw=0, duration=5.0)
        timeHelper.sleep(6.0)

        print("Landing...")
        allcfs.land(0.05, duration=4.0)
        timeHelper.sleep(3.0)