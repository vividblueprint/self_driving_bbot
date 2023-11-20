#include<ros/ros.h>
#include<std_msgs/String.h>

void callback(const std_msgs::String::ConstPtr& msg){
    ROS_INFO("New msg received: %s",msg->data.c_str());
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "listener");
    ros::NodeHandle nh;
    ros::Subscriber subscriber = nh.subscribe<std_msgs::String>("chatter", 10, callback);
    ros::spin();

    return 0;
}