import numpy as np
from pycrazyswarm import *

if __name__ == '__main__':
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    ids = [11]
    cfs = [allcfs.crazyfliesById[i] for i in ids]

    print("Taking off...\n")
    cfs[0].takeoff(targetHeight=1.0, duration=2.0)
    timeHelper.sleep(3.0)

    # while(True):
    #     print("Moving up")
    #     for i in range(500):
    #         cfs[0].cmdPosition([1., 0., 3.])
    #         timeHelper.sleep(0.01)
    #
    #     print("Moving down")
    #     for i in range(500):
    #         cfs[0].cmdPosition([1., 0., 2.])
    #         timeHelper.sleep(0.01)

    while(True):
        print("Moving up")
        for i in range(50):
            cfs[0].cmdFullState(pos=[1., -2., 2.], vel=[0,0,0], acc=[0,0,0],yaw=0, omega=[0,0,0])
            timeHelper.sleep(0.1)

        print("Moving down")
        for i in range(50):
            cfs[0].cmdFullState(pos=[1., 2., 2.], vel=[0,0,0], acc=[0,0,0],yaw=0, omega=[0,0,0])
            timeHelper.sleep(0.1)
