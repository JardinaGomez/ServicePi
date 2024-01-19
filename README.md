# ServicePi
### The following work was submitted as a Robotics project at Siena College. The project ServicePi is an autonomous servicedog robot. 


## Decription
 “ServicePi” is a robotic guide programmed to emulate the functionality of a service dog. For perception we used a LIDAR scanner, for mapping and obstacle detection, and utilized ‘sensor_msgs’ and ‘rplidar_ros’ for comprehensive environmental awareness. For navigation, ‘move_base_msgs’ and ‘nav_nasgs’ were integrated for efficient route planning. As for obstacle avoidance, we utilized costmap_2D for mapping and avoidance. As well as the Teb Local Planner for both collision avoidance and dynamic path planning. For Localization and mapping , ‘robot_localization’ was used for accurate positioning and orientation. ‘Slam_gmapping” was used for simultaneous localization and mapping. For planning, ‘move_base and Teb_local_planner’ was used for path planning and execution. For the adaption to the environment, the routes based on real-time data from sensors and LIDAR were adjusted. 

## Instructions
## 1. Install Dependencies 
###    rf2o_laser_odometry
###    move_base
###    Teb_local_planner
###    costmap_2d
###    robot_localization
###    slam_gmapping
## 2. Build Workspace 
###     In ** /catkin_ws** run the command:
###        ** catkin_make **
## 3. Source Setuo File 
###     Run the following command: 
###         ** Source ~/catkin_ws/devel/setup.bash **
## 4. Launch StartUp 
### Run the command 
###     ** roslaunch servicePi robot_startup.launch **
###     ** roslaunch servicePi navigation.launch **
## 5.  Run the executable for controlling behavior 
### Run the command 
###     ** rosrun servicePi robot_behavior.py **
###     ** rosrun servicePi simpleOps.py **

