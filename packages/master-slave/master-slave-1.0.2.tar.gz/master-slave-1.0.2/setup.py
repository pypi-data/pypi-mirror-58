from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name='master-slave',
    version='1.0.2',
    description='package to communicate with infected devices trought a local network',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Skorii/Python-Henallux-Project-2019',
    author='Arnaud "Skorii" Gony',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
    ],
    packages=['master_slave'],
    include_package_data=True,
    install_requires=['psutil', 'requests'],
    entry_points={
        "console_scripts": [
            "master = master_slave.master:main",
            "slave = master_slave.slave:main",
        ],
    },
    python_requires='>=3.0.',
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/Skorii/Python-Henallux-Project-2019/issues',
        'Source': 'https://github.com/Skorii/Python-Henallux-Project-2019',
    },
)
