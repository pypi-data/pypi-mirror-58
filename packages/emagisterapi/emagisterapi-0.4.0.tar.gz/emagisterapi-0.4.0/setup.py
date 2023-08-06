from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="emagisterapi",
    packages=['emagapi',],
    version="0.4.0",
    author="Cisco Delgado",
    author_email="fdelgados@gmail.com",
    description="Emagister public API connector",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fdelgados/EmagisterAPI.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests']
)
