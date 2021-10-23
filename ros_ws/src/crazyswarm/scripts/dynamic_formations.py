#!/usr/bin/env python
import numpy as np
from pycrazyswarm import *


def generate_init_goals(num_agents=8, formation_size=2.0, z_value=1.5):
    goals = []
    for i in range(num_agents):
        degree = 2 * np.pi * i / num_agents
        pos_0 = formation_size * np.cos(degree)
        pos_1 = formation_size * np.sin(degree)
        goal = np.array([pos_0, pos_1, z_value])
        goals.append(goal)
    return np.array(goals)


def get_new_goal(num_agents, formation_size, max_formation_size, z_value, increase_formation_size):
    new_goals = []
    control_speed = 1.0
    if formation_size <= -1.0 * max_formation_size:
        increase_formation_size = True
        control_speed = np.random.uniform(low=1.0, high=3.0)
    elif formation_size >= max_formation_size:
        increase_formation_size = False
        control_speed = np.random.uniform(low=1.0, high=3.0)

    if increase_formation_size:
        formation_size += 0.1 * control_speed
    else:
        formation_size -= 0.1 * control_speed

    for i in range(num_agents):
        degree = 2 * np.pi * i / num_agents
        pos_0 = formation_size * np.cos(degree)
        pos_1 = formation_size * np.sin(degree)
        goal = np.array([pos_0, pos_1, z_value])
        new_goals.append(goal)

    return np.array(new_goals), formation_size, increase_formation_size


if __name__ == '__main__':
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf_array = allcfs.crazyflies
    num_agents = 8
    # ids = [3, 17, 20, 27, 28, 33, 41, 47]
    ids = [3, 17, 20, 27]

    z = 1.5

    print("Taking off... \n")
    allcfs.takeoff(targetHeight=z, duration=3.0)
    timeHelper.sleep(4.0)

    print("Moving to goal..\n")

    formation_size = 2.0
    max_formation_size = 2.0
    increase_formation_size = False
    goals = generate_init_goals(formation_size=formation_size, z_value=z)

    for i, cfid in enumerate(ids):
        allcfs.crazyfliesById[cfid].goTo(goal=goals[i], yaw=0, duration=4.0)
    timeHelper.sleep(4.0)

    for t in range(0, 80):
        goals, formation_size, increase_formation_size = get_new_goal(num_agents, formation_size, max_formation_size, z, increase_formation_size)
        for i, cfid in enumerate(ids):
            allcfs.crazyfliesById[cfid].cmdPosition(pos=goals[i])
        timeHelper.sleep(0.1)

    poses = []
    for cfid in ids:
        curPos = allcfs.crazyfliesById[cfid].position()
        poses.append(curPos)

    # hold pose for 3.0 seconds
    for _ in range(30):
        for i, cfid in enumerate(ids):
            allcfs.crazyfliesById[cfid].cmdPosition(poses[i])
        timeHelper.sleep(0.1)

    # manually land over 5 seconds
    for _ in range(50):
        for i, cfid in enumerate(ids):
            curPos = poses[i]
            curPos -= np.array([0., 0., 0.05])
            allcfs.crazyfliesById[cfid].cmdPosition(curPos)
        timeHelper.sleep(0.1)





    # for cfid in ids:
    #     allcfs.crazyfliesById[cfid].goTo(goal=curPos, yaw=0, duration=3.0)
    # timeHelper.sleep(4.0)
    #
    # print("landing\n")
    # allcfs.land(0.04, duration=4.0)
    # timeHelper.sleep(3.0)
