from setuptools import setup
with open ("readme.md", "r") as fh:
    long_desc = fh.read()
setup(
    name='RustyWarePeople',
    version='0.0.1',
    description='Some people to extract',
    py_modules=["MyPeople"],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    long_description=long_desc,
    long_description_content_type="text/markdown",
)