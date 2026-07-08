from setuptools import setup,find_packages
with open("requirements.txt") as f:
    requirements=f.read().splitlines()
setup(
    name="MAF",
    author="Dhivya",
    packages=find_packages(),
    install_requires=requirements
)