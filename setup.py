
#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='brentlab_utils',
    version='0.0.1',
    description='A collection of python functions and objects useful in the brentlab',
    url='http://github.com/none_yet',
    author='Chase Mateusiak',
    author_email='chasem@wustl.edu',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        "pandas>=1.2.3",
        "requests"
    ],
    zip_safe=False
)


# setup(name='capitalize',
#       version = '1.0',
#       # list folders, not files
#       packages = ['capitalize','capitalize.test'],
#       scripts = ['bin/cap_script.py'],
#       package_data = {'capitalize': ['data/cap_data.txt']},
#       )