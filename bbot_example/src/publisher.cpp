#include<ros/ros.h>
#include<std_msgs/String.h>
#include<sstream>

using namespace std;

int main(int argc, char **argv)
{
    ros::init(argc,argv,"talker");
    ros::NodeHandle nh;
    ros::Publisher chatter = nh.advertise<std_msgs::String>("chatter", 10);
    ros::Rate rate(10);

    int count = 0;
    while(ros::ok()){
        std_msgs::String msg;
        std::stringstream ss;

        ss<<"Hello World from c++: "<<count;
        msg.data=ss.str();
        
        ROS_INFO("%s",msg.data.c_str());

        chatter.publish(msg);
        ros::spinOnce();
        rate.sleep();
        ++count;
    }

    return 0;
}