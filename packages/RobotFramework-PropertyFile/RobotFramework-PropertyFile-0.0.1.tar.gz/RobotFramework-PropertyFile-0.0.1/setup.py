import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="RobotFramework-PropertyFile",
    version="0.0.1",
    description="An utility package for exposing Java-style properties from property-files as variables in Robot Framework",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AdamHepner/robotframework-propertyfile",
    author="Adam Hepner",
    author_email="adam@hepner.eu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["robotframework_propertyfile"],
    include_package_data=True,
    install_requires=["jproperties", "robotframework"],
)