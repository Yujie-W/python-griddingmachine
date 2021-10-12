import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="python-griddingmachine",
    version="0.1.0",
    description="GriddingMachine - a database and tool for earth system modeling",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Yujie-W/python-griddingmachine",
    author="Yujie Wang",
    author_email="jesiner@gmail.com",
    license="Apache 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["griddingmachine"],
    include_package_data=True,
    install_requires=["numpy"],
    entry_points={},
)
