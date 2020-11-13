from setuptools import find_packages, setup

with open("README.md", "r") as f:
    DESCRIPTION = f.read()

setup(name="pymagnitude-light",
      version="0.1.143",
      description="Magnitude fork that only supports Word2Vec, GloVe and fastText embeddings",
      long_description=DESCRIPTION,
      long_description_content_type="text/markdown",
      url="https://github.com/davebulaval/magnitude-light",
      license="MIT",
      packages=find_packages(exclude=["tests", "tests.*"]),
      install_requires=[
        "fasteners>=0.14.1",
        "lz4>=1.0.0",
        "numpy>=1.14.0",
        "xxhash>=1.0.1"
      ] 
)
