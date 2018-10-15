import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testpackage",
    version="0.0.1",
    author="Onshape",
    description="A python wrapper around Onshape's REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "requests-toolbelt"
    ]
)
