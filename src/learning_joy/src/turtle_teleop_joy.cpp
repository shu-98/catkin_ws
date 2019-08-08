#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <sensor_msgs/Joy.h>


class TeleopTurtle
{
public:
  TeleopTurtle();

private:
  void joyCallback(const sensor_msgs::Joy::ConstPtr& joy);

  ros::NodeHandle nh_;

  int linear_, angular_;
  double l_scale_, a_scale_;
  ros::Publisher vel_pub_;
  ros::Publisher vel_pub2_; /* ←追加 */
  ros::Publisher vel_pub3_; /* ←追加 */
  ros::Subscriber joy_sub_;
};

TeleopTurtle::TeleopTurtle():
  linear_(1),
  angular_(2)
{

  nh_.param("axis_linear", linear_, linear_);
  nh_.param("axis_angular", angular_, angular_);
  nh_.param("scale_angular", a_scale_, a_scale_);
  nh_.param("scale_linear", l_scale_, l_scale_);

  vel_pub_ = nh_.advertise<geometry_msgs::Twist>("turtle1/cmd_vel", 1);
  vel_pub2_ = nh_.advertise<geometry_msgs::Twist>("cmd_vel", 1);          /* ←追加 */
  vel_pub3_ = nh_.advertise<geometry_msgs::Twist>("cmd_JC", 1);          /* ←追加 */

  joy_sub_ = nh_.subscribe<sensor_msgs::Joy>("joy", 10, &TeleopTurtle::joyCallback, this);
}


void TeleopTurtle::joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
{
  geometry_msgs::Twist twist;
  twist.angular.z = a_scale_*joy->axes[angular_];
  twist.linear.x = l_scale_*joy->axes[linear_];
  ROS_INFO("an.x:%f, an.y:%f, an.z:%f, li.x:%f, li.y:%f, li.z:%f", twist.angular.x, twist.angular.y, /*twist.angular.z*/joy->axes[angular_], /*twist.linear.x*/joy->axes[linear_], twist.linear.y, twist.linear.z);
  vel_pub_.publish(twist);
  vel_pub2_.publish(twist);     /* ←追加 */
  vel_pub3_.publish(twist);     /* ←追加 */
}


int main(int argc, char** argv)
{
  ros::init(argc, argv, "teleop_turtle");
  TeleopTurtle teleop_turtle;

  ros::spin();
}
