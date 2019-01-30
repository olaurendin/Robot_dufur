#!/usr/bin/env python

import roslib
import rospy , tf
from gazebo_msgs.srv import DeleteModel, SpawnModel, GetModelState
from geometry_msgs.msg import *

if __name__ == '__main__':
    rospy.init_node('weed_killer')

    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
	    print("ok")
            (trans,rot) = listener.lookupTransform('/chassis', '/cameraBras_link', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
	    print("fail")
            continue

    print("Waiting for gazebo services...")
    # rospy.init_node("laser_node")
    rospy.wait_for_service("gazebo/delete_model")
    rospy.wait_for_service("gazebo/spawn_sdf_model")
    rospy.wait_for_service("gazebo/get_model_state")

    print("Got it.")
    delete_model = rospy.ServiceProxy("gazebo/delete_model", DeleteModel)
    spawn_model = rospy.ServiceProxy("gazebo/spawn_sdf_model", SpawnModel)
    get_model_state = rospy.ServiceProxy("gazebo/get_model_state", GetModelState)
    # print(get_model_state("floor", "plant0"))

    # orient = Quaternion(0,0,0,0) #tf.transformations.quaternion_from_euler(0,0,0))

    # with open("../../worlds/plant.urdf", "r") as f:
    #     product_xml = f.read()
    plants = [i for i in range(nb_plants)]
    l_dists = []
    for i in plants:
        plant_name="plant{}".format(i)
        l_dists.append(get_model_state("floor", plant_name))
        # x = p.pose.position.x
        # y = p.pose.position.y
        # z = p.pose.position.z
    ind = np.argmin(l_dists)
    plants.pop(ind)
    delete_model("plant{}".format(ind))
        # spawn_model(plant_name, product_xml, "", item_pose, "world")
