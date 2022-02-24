from setuptools import setup, find_packages

setup(
    name='photoprism',
    version='1.0.0',
    packages=find_packages(exclude=['examples', 'tests']),
    install_requires=[
        'requests',
    ],
)
