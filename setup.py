from setuptools import find_packages, setup

from dichalcogenides import __version__

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='dichalcogenides',
    version=__version__,
    author='Evan Sosenko',
    author_email='razorx@evansosenko.com',
    packages=find_packages(exclude=['docs']),
    url='https://github.com/razor-x/dichalcogenides',
    license='MIT',
    description='Python analysis code for dichalcogenide systems.',
    long_description=long_description,
    test_suite='nose2.collector.collector',
    install_requires=[
        'numpy>=1.11.0,<2.0.0',
        'scipy>=0.17.0,<1.0.0',
        'pyyaml>=3.11,<4.0'
    ]
)
