# COMP150 Reinforcement Learning: Using RL to teach the Turtlebot avoid moving obstacles
<img src=https://github.com/js0823/pedsim_ros/blob/master/pedsim_simulator/images/screenshot1.png width=400/>



### Requirements
- ROS-kinetic full desktop install
- ROS turtlebot and gazebo packages (I recommend updating gazebo 7.0.0, the default gazebo version, to 7.14.0)

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
