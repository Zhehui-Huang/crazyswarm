#!/usr/bin/env python

import numpy as np
from pycrazyswarm import *

Z = 1.5

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    allcfs.takeoff(targetHeight=Z, duration=1.0+Z)
    timeHelper.sleep(1.5+Z)
    for cf in allcfs.crazyflies:
        init_pos = np.array(cf.initialPosition)
        pos = init_pos + np.array([0, 0, Z])
        cf.goTo(np.array([0, 0, Z]), 0, 3.0)

    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()

    allcfs.land(targetHeight=0.02, duration=1.0+Z)
    timeHelper.sleep(1.0+Z)
