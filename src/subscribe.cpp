
/********************************************************************
* Description: A simple ROS subscriber example to show the general  *
*   layout and flow of how to properly construct a subscriber.      *
*                                                                   *
* Author: Thomas Colestock (credit to ROS Tutorials)                *
* FAU BioRobotics Lab                                               *
*                                                                   *
********************************************************************/

#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Float32.h"
#include <sstream>


void callback(const std_msgs::String::ConstPtr& msg) {
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv) {
  // initialize and make node handle
  ros::init(argc, argv, "listener");
  ros::NodeHandle nh;

  // make subscriber and specify topic, buffer?, and callback
  ros::Subscriber sub = nh.subscribe("test_pub", 1000, callback);
  ros::spin();  // keep node alive

  return 0;
}
