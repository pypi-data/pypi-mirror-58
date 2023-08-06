import setuptools
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="icsdscraper",
    version="0.0.4",
    author="Achilleas Papakonstantinou",
    author_email="achipap@hotmail.com",
    description="ICSD website scraper",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/CheatModeON/icsd-scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
