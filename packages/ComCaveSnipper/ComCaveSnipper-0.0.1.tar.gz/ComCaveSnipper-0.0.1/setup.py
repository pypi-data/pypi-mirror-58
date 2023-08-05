import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ComCaveSnipper",
    version="0.0.1",
    author="ginnie3112x",
    author_email="ginnie3112x@gmail.com",
    description="Auto insert PIN in ComeCave Launcher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ginnie3112x@dev.azure.com/ginnie3112x/ComeCaveSnipper/_git/ComeCaveSnipper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)