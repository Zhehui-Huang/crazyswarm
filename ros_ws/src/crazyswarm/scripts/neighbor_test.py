#!/usr/bin/env python

import numpy as np

from pycrazyswarm import *

if __name__ == '__main__':
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf_array = allcfs.crazyflies

    Z = 2.0

    ids = [3, 41]
    cfs = [allcfs.crazyfliesById[i] for i in ids]
    allcfs.takeoff(targetHeight=Z, duration=3.0)
    timeHelper.sleep(5.0)

    poses = [np.array(cf.position()) for cf in cfs]
    cfs[1].goTo(poses[0], yaw=0, duration=3.0)
    timeHelper.sleep(5.0)
    cfs[1].goTo(poses[1], yaw=0, duration=3.0)
    timeHelper.sleep(3.0)
    allcfs.land(targetHeight=0.04, duration=3.0)
    timeHelper.sleep(2.0)
