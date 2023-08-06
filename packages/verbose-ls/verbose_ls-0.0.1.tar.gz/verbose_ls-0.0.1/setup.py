from setuptools import find_packages, setup

VERSION = "0.0.1"

setup(
    name="verbose_ls",
    version=VERSION,
    description="Format 'ls' output into verbose, human readable output",
    url="https://github.com/NelsonScott/verbose_ls",
    packages=find_packages(),
    entry_points={"console_scripts": ["verbose_ls = verbose_ls:main"]},
    include_package_data=True,
    python_requires=">=3.7",
)
