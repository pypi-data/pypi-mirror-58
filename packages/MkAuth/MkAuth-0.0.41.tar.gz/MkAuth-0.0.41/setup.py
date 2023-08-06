import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MkAuth",
    version="0.0.41",
    author="Mark Cartagena",
    author_email="mark@mknxgn.com",
    description="MkNxGn User Management. Free for use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://mknxgn.com/",
    requires=['mknxgn_essentials', 'flask'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)