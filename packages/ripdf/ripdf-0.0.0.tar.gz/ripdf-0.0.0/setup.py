import setuptools
from pathlib import Path

setuptools.setup(
    name="ripdf",
    virsion=1.0,
    long_description=Path("README.md").read_text(),
    Packages=setuptools.find_packages(exclude=["tests", "data"])
)
