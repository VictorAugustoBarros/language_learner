"""Módulo Setup."""
from setuptools import setup, find_packages

setup(
    name='learner',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'learner=app.main:cli'
        ],
    },
)
