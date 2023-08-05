import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="chnutils",
    version="0.0.6",
    author="Drew Stinnett",
    author_email="drew.stinnett@duke.edu",
    description=("Helper scripts for CHN"),
    install_requires=install_requirements,
    license="LGPL 2.1",
    keywords="chn",
    scripts=['scripts/chn-register.py'],
    long_description_content_type="text/markdown",
    long_description=read('README.md'),
)
