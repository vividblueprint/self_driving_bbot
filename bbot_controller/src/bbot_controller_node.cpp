#include <ros/ros.h>
#include "bbot_controller/bbot_controller.h"


int main(int argc, char **argv)
{
    ros::init(argc, argv, "bbot_controller");
    ros::NodeHandle nh;
    ros::NodeHandle pnh("~");
    double wheel_radius, wheel_separation;
    pnh.getParam("wheel_radius", wheel_radius);
    pnh.getParam("wheel_separation", wheel_separation);
    Bbot_controller controller(nh, wheel_radius, wheel_separation);
    ros::spin();

    return 0;
}