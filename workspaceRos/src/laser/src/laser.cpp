// #include "ros/ros.h"
// #include "gazebo_msgs/SpawnModel.h"
//
// bool apply_laser(gazebo_msgs::Request  &req,
//   gazebo_msgs::Response &res)
// {
//   ROS_INFO("request: plant at x=%ld, y=%ld, z=%ld", (long int)req.initial_pose.x, (long int)req.initial_pose.y, (long int)req.initial_pose.z);
//   ROS_INFO("sending back response: [%s]", status_message);
//   return true;
// }
//
// int main(int argc, char **argv)
// {
//   ros::init(argc, argv, "laser_handler");
//   ros::NodeHandle n;
//
//   ros::ServiceServer service = n.advertiseService("gazebo/spawn_urdf_model", apply_laser);
//   ROS_INFO("Ready to add two ints.");
//   ros::spin();
//
//   return 0;
// }

#include "ros/ros.h"
#include "gazebo_msgs/SpawnModel.h"
#include <cstdlib>

int main(int argc, char **argv)
{
  // ros::init(argc, argv, "gazebo/spawn_urdf_model");

  string init_plant()

  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<gazebo_msgs::SpawnModel>("add_two_ints");
  gazebo_msgs::SpawnModel srv;
  srv.request.model_name = "extra_plant"
  srv.request.model_xml =
  srv.request.initial_pose.position.x = 0
  srv.request.initial_pose.position.y = 0
  srv.request.initial_pose.position.z = 0
  srv.request.initial_pose.orientation.x = 0
  srv.request.initial_pose.orientation.y = 0
  srv.request.initial_pose.orientation.z = 0
  srv.request.initial_pose.orientation.w = 0

  srv.request.a = atoll(argv[1]);
  srv.request.b = atoll(argv[2]);
  if (client.call(srv))
  {
    ROS_INFO("Sum: %ld", (long int)srv.response.sum);
  }
  else
  {
    ROS_ERROR("Failed to call service add_two_ints");
    return 1;
  }

  return 0;
}
