#include <rclcpp/rclcpp.hpp>
#include <vector>
#include <string>

struct WayPoint {
    double latitude;
    double longitude;
    double altitude;
};

class GPSNavigation : public rclcpp::Node {
public:
    GPSNavigation() : Node("yaml_test") {
        // Declare parameters
        declare_parameter<double>("navigation.radius", 2.0);
        declare_parameter<int>("navigation.waypoints_A.count", 0);
        declare_parameter<int>("navigation.waypoints_B.count", 0);

        for (int i = 0; i < 7; ++i) {
            std::string param_prefix = "navigation.waypoint_";
            
            declare_parameter<double>("navigation.waypoints_A.waypoint_" + std::to_string(i) + ".latitude", 2.0);
            declare_parameter<double>("navigation.waypoints_A.waypoint_" + std::to_string(i) + ".longitude", 2.0);
            declare_parameter<double>("navigation.waypoints_A.waypoint_" + std::to_string(i) + ".altitude", 2.0);
            
            declare_parameter<double>("navigation.waypoints_B.waypoint_" + std::to_string(i) + ".latitude", 2.0);
            declare_parameter<double>("navigation.waypoints_B.waypoint_" + std::to_string(i) + ".longitude", 2.0);
            declare_parameter<double>("navigation.waypoints_B.waypoint_" + std::to_string(i) + ".altitude", 2.0);
        }

        // Initial parameter load
        load_parameters();

        // Create timer for periodic parameter loading (1 second interval)
        timer_ = create_wall_timer(
            std::chrono::seconds(1),
            std::bind(&GPSNavigation::load_parameters, this)
        );
    }

private:
    double radius_;
    std::vector<WayPoint> waypoints_A_;
    std::vector<WayPoint> waypoints_B_;
    rclcpp::TimerBase::SharedPtr timer_;

    void load_parameters() {
        // Access parameters using dotted notation
        radius_ = get_parameter("navigation.radius").as_double();
        waypoints_A_ = load_waypoints("A");
        waypoints_B_ = load_waypoints("B");

        RCLCPP_INFO(get_logger(), "Parameters updated:");
        RCLCPP_INFO(get_logger(), "Radius: %.2f", radius_);
        RCLCPP_INFO(get_logger(), "Waypoints A: %zu", waypoints_A_.size());
        RCLCPP_INFO(get_logger(), "Waypoints B: %zu", waypoints_B_.size());
    }

    std::vector<WayPoint> load_waypoints(const std::string& trajectory) {
        std::vector<WayPoint> waypoints;
        std::string prefix = "navigation.waypoints_" + trajectory;

        // Get the number of waypoints
        int count = get_parameter(prefix + ".count").as_int();
        RCLCPP_INFO(get_logger(), "Count: %d", count);

        // Load each waypoint
        for (int i = 0; i < count; ++i) {
            std::string wp_prefix = prefix + ".waypoint_" + std::to_string(i);
            try {
                WayPoint wp;
                wp.latitude = get_parameter(wp_prefix + ".latitude").as_double();
                wp.longitude = get_parameter(wp_prefix + ".longitude").as_double();
                wp.altitude = get_parameter(wp_prefix + ".altitude").as_double();
                RCLCPP_INFO(get_logger(), "Waypoint: latitude: %f, longitude: %f, altitude: %f", wp.latitude, wp.longitude, wp.altitude);
                waypoints.push_back(wp);
            } catch (const rclcpp::ParameterTypeException& e) {
                RCLCPP_ERROR(get_logger(), "Failed to load waypoint %d: %s", i, e.what());
            }
        }

        return waypoints;
    }
};

int main(int argc, char** argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<GPSNavigation>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}