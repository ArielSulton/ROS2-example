from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="pkg_cpp",
            executable="pubs_cpp",
            name="pubs_cpp",
            output="screen",
            emulate_tty=True,
        ),
        Node(
            package="pkg_cython",
            executable="subs_cy",
            name="subs_cy",
            output="screen",
            emulate_tty=True,
        ),
        Node(
            package="pkg_python",
            executable="subs_py",
            name="subs_py",
            output="screen",
            emulate_tty=True,
            parameters=[
                {}
            ]
        )
    ])