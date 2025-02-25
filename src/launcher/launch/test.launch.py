import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, LogInfo
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.conditions import IfCondition

def generate_launch_description():
    # ros2 param load <node_name> <parameter_file>
    # ros2 param load yaml_node ~/ros2_ws/src/launcher/config/test.yaml 
    
    return LaunchDescription([
        Node(
            package="pkg_yaml",
            executable="yaml_test",
            name="yaml_node",
            output="screen",
            emulate_tty=True,
            parameters=[
                os.path.join(
                    get_package_share_directory('launcher'),
                    'config',
                    'test.yaml'
                )
            ],   
        ),
        # Node(
        #     package="pkg_cpp",
        #     executable="pubs_cpp",
        #     name="pubs_cpp",
        #     output="screen",
        #     emulate_tty=True,
        # ),
        # Node(
        #     package="pkg_cython",
        #     executable="subs_cy",
        #     name="subs_cy",
        #     output="screen",
        #     emulate_tty=True,
        # ),
        # Node(
        #     package="pkg_python",
        #     executable="subs_py",
        #     name="subs_py",
        #     output="screen",
        #     emulate_tty=True,
        #     parameters=[
        #         {}
        #     ]
        # ),
        # Node(
        #     package="pkg_python",
        #     executable="pubs_py",
        #     name="pubs_py",
        #     output="screen",
        #     emulate_tty=True,
        # ),
        # Node(
        #     package="pkg_python2",
        #     executable="pubs_py",
        #     name="pubs_py2",
        #     output="screen",
        #     emulate_tty=True,
        #     parameters=[
        #         os.path.join(
        #             get_package_share_directory('launcher'),
        #             'config',
        #             'test.yaml'
        #         )
        #     ]
        # )
    ])