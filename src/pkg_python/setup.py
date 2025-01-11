from setuptools import setup

package_name = 'pkg_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arielsulton',
    maintainer_email='arielsulton26@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            #'random_name/node_name = pkg_name.exe_name/file_name:main'
            'pubs_py = pkg_python.pubs_py:main',
            'subs_py = pkg_python.subs_py:main'
        ],
    },
)
