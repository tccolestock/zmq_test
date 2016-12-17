
/********************************************************************
* Description: A simple ros publisher example to show the general   *
*   layout and flow of how to properly construct a publisher.       *
*                                                                   *
* Author: Thomas Colestock (credit to ROS Tutorials)                *
* FAU BioRobotics Lab                                               *
*                                                                   *
********************************************************************/

#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Float32.h"
#include <sstream>


int main(int argc, char **argv) {

  // initialize and make node handle
  ros::init(argc, argv, "talker");
  ros::NodeHandle nh;

  // create publisher and specify rate
  ros::Publisher pub = nh.advertise<std_msgs::String>("test_pub", 100);
  ros::Rate rate_handle(10); //hz

  // while ros is not shutdown, publish the string
  while (ros::ok())
  {
    std_msgs::String msg;  // make a ros String message type 'msg'
    std::stringstream ss;  // make a stringstream 'ss'
    ss << "hello world";
    msg.data = ss.str();  // assign the stringstream data to the ros String msg type .data
    ROS_INFO("%s", msg.data.c_str());  // log ros info
    pub.publish(msg);
    ros::spinOnce();  // keep node alive and process one cycle
    rate_handle.sleep();  // maintain proper rate

  }
  return 0;
}
