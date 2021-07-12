import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='btshelloworldpkg',  
    version='0.1',
    author="Blue Thunder Somogyi",
    author_email="btsomogyi@verta.ai",
    description="hello world!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bts-verta/helloworld",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )
