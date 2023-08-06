from setuptools import find_packages, setup

with open("README.rst", "r") as longdesc:
    long_description = longdesc.read()


setup(
    name="pyuf",
    description="Union-Find data structure implementation in Python",
    long_description=long_description,
    author="Mariano Anaya",
    version="0.1.1",
    license="MIT",
    author_email="marianoanaya@gmail.com",
    packages=find_packages(where="src/"),
    package_dir={"": "src"},
    extras_require={"dev": ["pytest", "black", "flake8"]},
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
