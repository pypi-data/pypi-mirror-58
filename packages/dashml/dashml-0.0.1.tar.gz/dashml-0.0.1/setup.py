import setuptools


with open("README.md") as file:
    long_desc = file.read()


setuptools.setup(
    name="dashml",
    version="0.0.1",
    author="Madelyn Eriksen",
    author_email="opensource@madelyneriksen.com",
    description="Generate HTML with Python functions.",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/madelyneriksen/dashml",
    packages=["dashml"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
