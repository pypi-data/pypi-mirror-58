"""
setup.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

from setuptools import setup


# Read version
with open('version.yml', 'r') as f:
    data = f.read().splitlines()
version_dict = dict([element.split(': ') for element in data])

# Convert the version_data to a string
version = '.'.join([str(version_dict[key]) for key in ['major', 'minor', 'patch']])

# Read in requirements.txt
# with open('requirements.txt', 'r') as f:
#     requirements = f.read().splitlines()

# Setup
setup(
    name='gitpipe',
    version=version,
    author='C. Lockhart',
    author_email='chris@lockhartlab.org',
    description='Connect to git through subprocess in Python',
    long_description='Connect to git through subprocess in Python',
    long_description_content_type='text/x-rst',
    url="https://www.lockhartlab.org",
    packages=[
        'gitpipe',
    ],
    install_requires=[],
    include_package_data=True,
    zip_safe=True
)
