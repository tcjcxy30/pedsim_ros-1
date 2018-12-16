# Python file for launching DQN using lidar to learn.

import gym
from gym import wrappers
import time
from distutils.dir_util import copy_tree
import os
import json
import liveplot
import dqn

def detect_monitor_files(training_dir):
    return [os.path.join(training_dir, f) for f in os.listdir(training_dir) if f.startswith('openaigym')]

def clear_monitor_files(training_dir):
    files = detect_monitor_files(training_dir)
    if len(files) == 0:
        return
    for file in files:
        print(file)
    os.unlink(file)

if __name__ == '__main__':
    env = gym.make('GazeboCircuit2TurtlebotLidarNn-v0')
    outdir = '/tmp/gazebo_gym_experiments/'
    path = '/tmp/turtle_c2_dqn_ep'
    plotter = liveplot.LivePlot(outdir)