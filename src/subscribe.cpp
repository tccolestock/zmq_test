#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Float32.h"
// #include "zhelpers.hpp"
#include "turtlesim/Color.h"
#include <sstream>

/* Subscribes to a ROS topic and republishes it to ZMQ */

void callback(const std_msgs::String::ConstPtr& msg) {
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "listener");
  ros::NodeHandle nh;

  // zmp::context_t context(1);
  // zmq::socket_t publisher(context, ZMQ_PUB);
  // publisher.bind("tcp://5557");

  ros::Subscriber sub = nh.subscribe("test_pub", 1000, callback);
  ros::spin();
  return 0;
}
