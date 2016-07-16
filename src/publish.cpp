
#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Float32.h"
#include <sstream>


int main(int argc, char **argv) {

  //ros::init(argc, argv, "pub_test");
  ros::init(argc, argv, "talker");
  ros::NodeHandle nh;

  ros::Publisher pub = nh.advertise<std_msgs::String>("test_pub", 100);
  ros::Rate rate_handle(10); //hz

  while (ros::ok())
  {
    std_msgs::String msg;
    std::stringstream ss;
    ss << "hello world";
    msg.data = ss.str();
    ROS_INFO("%s", msg.data.c_str());
    pub.publish(msg);
    ros::spinOnce();
    rate_handle.sleep();

  }
  return 0;
}
