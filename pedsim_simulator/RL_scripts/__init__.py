import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

# Gazebo
# ----------------------------------------

# Turtlebot envs
register(
    id='pedsim-default-v0',
    entry_point='gym_pedsim.envs.turtlebot:GazeboMazeTurtlebotLidarEnv',
    # More arguments here
)