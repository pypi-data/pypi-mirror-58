import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ddx",
    version="0.0.2",
    author="ChanMo",
    author_email="chan.mo@outlook.com",
    description="快速搭建基于Docker的Django项目",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChanMo/ddx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
