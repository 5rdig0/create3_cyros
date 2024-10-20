from setuptools import setup
from setuptools import find_packages
import os
from glob import glob
package_name = 'create3_cam'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jkearns',
    maintainer_email='jkearns@irobot.com',
    description='Example ROS 2 Python code to use iRobot® Create® 3',
    license='BSD-3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'stream = create3_cam.server:main'
            'detect = create3_cam.detection:main'
        ],
    },
)
