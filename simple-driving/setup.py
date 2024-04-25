import os

from setuptools import find_packages, setup


setup(
    name="simple_driving",
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=["gymnasium>=0.26", "pybullet", "numpy","numpngw", "matplotlib"],
    
)
