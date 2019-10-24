# Simple planner
Vrep ROS interface with demo scene

(Realtime was previously activated on this scene)

## Install instructions
Build workspace with ```catkin_make```

## Execution instructions
1. Start ```roscore```

2. Update ros package list with ```source <workspace location>/devel/setup.bash```

3. Activate realtime simulation on ROS with ```rosparam set use_sim_time true```

4. Open ```test_maze``` scene on vrep


5. Execute ```rosrun simpleplanner path.py```
