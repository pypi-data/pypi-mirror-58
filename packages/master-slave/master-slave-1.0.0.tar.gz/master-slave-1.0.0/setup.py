from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name='master-slave',
    version='1.0.0',
    description='package to communicate with infected devices trought a local network',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Skorii/ProjetPython2019',
    author='Arnaud "Skorii" Gony',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['master_slave'],
    include_package_data=True,
    install_requires=['argparse', 'datetime', 'logging', 'os', 'platform', 'psutil', 're', 'requests', 'shutil', 'socket', 'threading', 'time', 'uuid'],
    entry_points={
        "console_scripts": [
            "master = master_slave.master:main",
            "slave = master_slave.slave:main",
        ],
    },
)
