import setuptools

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="icsdscraper",
    version="0.0.5",
    author="Achilleas Papakonstantinou",
    author_email="achipap@hotmail.com",
    description="ICSD website scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CheatModeON/icsd-scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
