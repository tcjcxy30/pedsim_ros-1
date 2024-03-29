# COMP150 Reinforcement Learning: Path Planning Amidst Moving Obstacles
<img src=https://github.com/js0823/pedsim_ros/blob/master/pedsim_simulator/images/screenshot1.png width=400/>

### Requirements
- Ubuntu 16 is required as this project uses ROS-kinetic which is compatible with Ubuntu 16.
- ROS-kinetic full desktop install by:
```
sudo apt install ros-kinetic-desktop-full
sudo apt install ros-kinetic-turtlebot ros-kinetic-turtlebot-gazebo ros-kinetic-turtlebot-apps ros-kinetic-turtlebot-rviz-launchers
```
Below is packages you may need, especially to use gym-gazebo in the future development.
```
sudo apt install ros-kinetic-octomap-msgs ros-kinetic-joy ros-kinetic-geodesy ros-kinetic-octomap-ros ros-kinetic-control-toolbox ros-kinetic-pluginlib ros-kinetic-trajectory-msgs ros-kinetic-control-msgs ros-kinetic-std-srvs ros-kinetic-nodelet ros-kinetic-urdf ros-kinetic-rviz ros-kinetic-kdl-conversions ros-kinetic-eigen-conversions ros-kinetic-tf2-sensor-msgs ros-kinetic-pcl-ros ros-kinetic-navigation cmake gcc g++ qt4-qmake libqt4-dev libusb-dev libftdi-dev python3-defusedxml python3-vcstool
```

- ROS turtlebot and gazebo packages (I recommend updating gazebo 7.0.0, the default gazebo version, to 7.14.0)
```
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable lsb_release -cs main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install gazebo7
gazebo --version (should return 7.14.0 or above)
```
- Setting up python2 using anaconda

If you want to use python from anaconda, you need to install the following package in anaconda python by running commands below.
```
pip install catkin_pkg
pip install rospkg
```
Then follow below to install machine learning packages in anaconda python.
```
conda install keras
```

### Package Installation
Building our package is simple. Follow the command below.
```
cd [workspace]/src
git clone https://github.com/js0823/pedsim_ros.git  
cd pedsim_ros
git submodule update --init --recursive
cd ../..
catkin_make
```
Above will build our package. To make use of it, you need to source the setup.bash in devel folder. To do this, I recommend putting it in your .bashrc file by doing

```
echo "source [workspace]/devel/setup.bash" >> ~/.bashrc
```
At the end, you should have two lines in your .bashrc that relates to ROS. They are
```
source /opt/ros/kinetic/setup.bash
source [workspace]/devel/setup.bash
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
### License
Original pedsim_ros package is here https://github.com/srl-freiburg/pedsim_ros.
