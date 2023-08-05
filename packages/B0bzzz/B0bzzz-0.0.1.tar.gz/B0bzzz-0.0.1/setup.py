import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="B0bzzz", # Replace with your own username
    version="0.0.1",
    author="Joon VP",
    author_email="joon.paravisini@epitech.eu",
    description="A basic calculator project in Python",
    long_description="N/A",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)