"""Single CF: takeoff, follow absolute-coords waypoints, land."""

import numpy as np

from pycrazyswarm import Crazyswarm
import pdb

Z = 0.5
TAKEOFF_DURATION = 1.0
GOTO_DURATION = 1.0
WAYPOINTS = np.array([
    (0.0, -2.0, Z),
    (0.0, 0.0, Z),
])

ID = 8

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyfliesById[ID]
    # pdb.set_trace()
    # print(cf.__dir__)

    cf.takeoff(targetHeight=Z, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION + 0.5)
    print(cf.position())
    z = Z
    for _ in range(3):
        z += 0.2
        cf.goTo([0., 0., z], yaw=0.0, duration=GOTO_DURATION)
        print(cf.position())
        timeHelper.sleep(GOTO_DURATION + 0.5)
        print(cf.position())

    # cf.goTo([0., 0., 0.5], yaw=0.0, duration=6.0)
    # timeHelper.sleep(8.0)
    # print(cf.position())
    timeHelper.sleep(0.2)
    cf.land(targetHeight=0.05, duration=5.0)
    timeHelper.sleep(7.0)
    print(cf.position())


if __name__ == "__main__":
    main()
