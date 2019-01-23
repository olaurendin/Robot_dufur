#!/usr/bin/env python

import rospy #, tf
from gazebo_msgs.srv import DeleteModel, SpawnModel, GetModelState
from geometry_msgs.msg import *

if __name__ == '__main__':
    print("Waiting for gazebo services...")
    rospy.init_node("laser_node")
    rospy.wait_for_service("gazebo/delete_model")
    rospy.wait_for_service("gazebo/spawn_sdf_model")
    rospy.wait_for_service("gazebo/get_model_state")

    print("Got it.")
    delete_model = rospy.ServicePoxy("gazebo/delete_model", DeleteModel)
    spawn_model = rospy.ServiceProxy("gazebo/spawn_model", SpawnModel)
    get_model_state = rospy.ServiceProxy("gazebo/spawn_model", GetModelState)
    print(get_model_state("plant0")

    # with open("../worlds/plant.urdf", "r") as f:
    #     product_xml = f.read()
    #
    # orient = Quaternion(tf.transformations.quaternion_from_euler(0,0,0))

    # for num in xrange(0,12):
    #     item_name = "product_{0}_0".format(num)
    #     print("Deleting model:%s", item_name)
    #     delete_model(item_name)
    #
    # for num in xrange(0,12):
    #     bin_y   =   2.8 *   (num    /   6)  -   1.4
    #     bin_x   =   0.5 *   (num    %   6)  -   1.5
    #     item_name   =   "product_{0}_0".format(num)
    #     print("Spawning model:%s", item_name)
    #     item_pose   =   Pose(Point(x=bin_x, y=bin_y,    z=2),   orient)
    #     spawn_model(item_name, product_xml, "", item_pose, "world")
