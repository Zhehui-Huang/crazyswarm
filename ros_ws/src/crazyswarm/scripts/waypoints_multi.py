#!/usr/bin/env python
import numpy as np

from pycrazyswarm import Crazyswarm


Z = 1.0
TAKEOFF_DURATION = 3.0
GOTO_DURATION = 3.0
# WAYPOINTS = np.array([
#     (3.0, 0.0, Z),
#     (3.0, 3.0, Z),
#     (0.0, 3.0, Z),
#     (0.0, 0.0, Z),
# ])
WAYPOINTS = np.array([
    (1.5, -1.5, Z),
    (1.5, 1.5, Z),
    (-1.5, 1.5, Z),
    (-1.5, -1.5, Z),
])

if __name__ == '__main__':
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    # ids = [7, 12, 11, 10]
    ids = [17, 20, 33, 41]
    cfs = [allcfs.crazyfliesById[i] for i in ids]

    print("Taking off..\n")
    allcfs.takeoff(targetHeight=2.0, duration=2.5)
    timeHelper.sleep(TAKEOFF_DURATION + 1.0)

    print("Moving...\n")
    for p in WAYPOINTS:
        for cf in cfs:
            cf.goTo(p, yaw=0.0, duration=GOTO_DURATION)
        timeHelper.sleep(GOTO_DURATION + 1.0)

    print("Landing..\n")
    cf.land(targetHeight=0.0, duration=TAKEOFF_DURATION + 2.0)
    timeHelper.sleep(TAKEOFF_DURATION + 1.0)
    cf.land(targetHeight=0.0, duration=TAKEOFF_DURATION + 2.0)
    timeHelper.sleep(TAKEOFF_DURATION + 1.0)