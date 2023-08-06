import setuptools

def readme():
    with open('README.md') as f:
        return f.read()

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()
    
setuptools.setup(
    name="icsdscraper",
    version="0.0.8",
    author="Achilleas Papakonstantinou",
    author_email="achipap@hotmail.com",
    description="ICSD website scraper",
    long_description=long_description,
    #long_description="Scrapping professors and courses from [ICSD website](http://www.icsd.aegean.gr/icsd/)\nOriginal idea by [Yannis Alexiou](https://github.com/yannisalexiou). Check his implementation in NodeJS [here](https://www.npmjs.com/package/icsd-scraper)\nInstall package:- pip install icsd-scraper\nImport main library:\n- import PapaScrap\n## Functions\n### getProfessors\nReturns all professors as an array of objects with the below details:\n**name, academicRank, link, office, tel, email, website, image**\n### getBasicCourses\nReturns all courses as an array of objects with the below details:\n**title, code, semester, ects, theoryHours, labHours, professor, link**\n### getAdvancedCourses\nReturns all courses as an array of objects with the below details:\n**contentOutline, learningOutcomes, prerequisites, basicTextbooks, additionalReferences, teachingMethod, grandingMethod, languageOfInstruction, modeOfDelivery**\n**Ιmportant:** `getAdvancedCourses` doesn't always work properly due to lack of consistency of ICSD site. So it's better to use the `getBasicCourses` to retrieve basic course information.",
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
