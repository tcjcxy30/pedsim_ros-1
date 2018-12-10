# Pedestrian Simulator
<img src=https://github.com/srl-freiburg/pedsim_ros/blob/master/pedsim_simulator/images/screenshot1.png width=400/>

ROS packages for a 2D pedestrian simulator based on social force
model of [Helbing et. al](http://arxiv.org/pdf/cond-mat/9805244.pdf). The implementation is based on an extended version of Christian Gloor's [libpedsim](http://pedsim.silmaril.org/) library which has been extended to include additional behaviors and activities. This packages is useful for robot navigation experiments with crowded scenes which are hard to acquire in practice.


### Requirements
- ROS with the visualization stack (currently tested on `hydro`, `indigo`, `kinetic` )
- C++11 compiler

### Installation

```
cd [workspace]/src
git clone https://github.com/js0823/pedsim_ros.git  
cd pedsim_ros
git submodule update --init --recursive
cd ../..
catkin build -c  # or catkin_make
```

### Sample usage
Default method is to launch the turtlebot_RL.launch via this command.
```
roslaunch pedsim_simulator turtlebot_RL.launch
```
If you wish to control the turtlebot via keyboard, you can use this on your other terminal.
```
roslaunch pedsim_simulator keyboard_teleop.launch
```
### Licence
Original pedsim_ros is here https://github.com/srl-freiburg/pedsim_ros
