from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="publisher",
            executable="pubs",
            name="pubs",
            output="screen",
            emulate_tty=True,
        ),
        Node(
            package="subscriber",
            executable="subs",
            name="subs",
            output="screen",
            emulate_tty=True,
            parameters=[
                {}
            ]
        )
    ])