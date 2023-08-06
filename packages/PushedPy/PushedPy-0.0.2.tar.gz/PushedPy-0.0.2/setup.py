import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PushedPy",
    version="0.0.2",
    author="Mick Rasmussen",
    author_email="mira19@guldborgsund.dk",
    description="A Python wrapper for the Pushed.co API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mickras/PushedPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
