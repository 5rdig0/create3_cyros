from setuptools import setup
from setuptools import find_packages

package_name = 'create3_procedures'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'square = create3_procedures.dodge.square:main',
            'foward = create3_procedures.dodge.fowar:main'
        ],
    },
)