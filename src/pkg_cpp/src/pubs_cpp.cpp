#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

#include <chrono>
#include <functional>
#include <memory>
#include <string>

using namespace std::chrono_literals;

class MinimalPublisher : public rclcpp::Node {
  public:
    MinimalPublisher() : Node("pubs_cpp"), 
      count(0) 
    {
      this->publisher = this->create_publisher<std_msgs::msg::String>("topic", 10);
      this->timer = this->create_wall_timer(0.01ms, std::bind(&MinimalPublisher::timer_callback, this));
    }

  private:
    rclcpp::TimerBase::SharedPtr timer;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher;
    size_t count;
    
    void timer_callback() {
      auto message = std_msgs::msg::String();
      message.data = "Hello, world! " + std::to_string(this->count++);
      this->publisher->publish(message);
      RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
    }
};

int main(int argc, char * argv[]) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalPublisher>());
  rclcpp::shutdown();
  return 0;
}