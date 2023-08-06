import setuptools

with open("README.md",'r') as f:
    long_description = f.read()

setuptools.setup(
    name= "Larry-Add",
    version = '0.0.1',
    author="GeorgeTemu",
    author_email = "georgetemu123@gmail.com",
    description = 'A simple packaging prgm',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/pypi/sampleproject',
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.0',
)