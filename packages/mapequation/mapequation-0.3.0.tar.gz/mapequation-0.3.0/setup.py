import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mapequation",
    version="0.3.0",
    author="Anton Eriksson",
    author_email="anton.eriksson@umu.se",
    description="Map Equation codelength calculator for multilevel state networks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mapequation/mapequation-py",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
