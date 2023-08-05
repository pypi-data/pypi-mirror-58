import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="memgraph",
    version="0.0.1",
    author="Mahmoud Alfayoumi",
    author_email="mfayoumi.dev@gmail.com",
    description="In memory graph database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mfayoumi/memgraph",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)