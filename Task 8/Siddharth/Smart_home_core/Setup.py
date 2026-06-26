
from setuptools import find_packages, setup

package_name = 'smart_home_core'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='siddharth-prasad',
    maintainer_email='siddharth-prasad@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
	    'temp_sensor = smart_home_core.temp_sensor_node:main',
            'smart_plug = smart_home_core.smart_plug_node:main',
            'dashboard = smart_home_core.dashboard_node:main',
        ],
    },
)
