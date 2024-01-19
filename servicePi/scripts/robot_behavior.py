#1/usr/bin/env python3 
import rospy 
from sensor_msgs.msg import LaserScan 
from geometry_msgs.msg import Twist
import yaml
from control_msgs.msg import JointTrajectoryControllerState

def lidar_callback(data):

    #Process LIDAR data for obstacle avoidance 
    pass


def main():
    rospy.init_node('service_dog_robot')

    #Subscribers 
    rospy.Subscriber('/scan', LaserScan, lidar_callback)

    # Publishers 
    cmd_vel_pub = rospy.Publisher('/cmd/vel', Twist, queue_size=1)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        # Robot behavior logic 
        # Including obstacle avoidance, nav, etc

        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass



