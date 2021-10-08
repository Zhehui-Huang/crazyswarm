#!/usr/bin/env python

from pycrazyswarm import *

if __name__ == '__main__':
    swarm = Crazyswarm()
    allcfs = swarm.allcfs
    allcfs.land(0.0, duration=4.0)