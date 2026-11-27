from setuptools import find_packages, setup

package_name = 'pkg_agv_fms_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hzt',
    maintainer_email='hztmail1109@163.com',
    description='AGV FMS control node for VDA5050-based AGV movement simulation',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'agv_fms_control = pkg_agv_fms_control.agv_fms_control:main'
        ],
    },
)
