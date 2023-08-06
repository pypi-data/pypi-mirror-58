
Scrapping professors and courses from [ICSD website](http://www.icsd.aegean.gr/icsd/)

Original idea by [Yannis Alexiou](https://github.com/yannisalexiou). Check his implementation in NodeJS [here](https://www.npmjs.com/package/icsd-scraper)

Install package:
- pip install icsd-scraper
Import main library:
- import PapaScrap

## Functions 
### getProfessors
Returns all professors as an array of objects with the below details:

**name, academicRank, link, office, tel, email, website, image**

### getBasicCourses
Returns all courses as an array of objects with the below details:

**title, code, semester, ects, theoryHours, labHours, professor, link**

### getAdvancedCourses
Returns all courses as an array of objects with the below details:

**contentOutline, learningOutcomes, prerequisites, basicTextbooks, additionalReferences, teachingMethod, grandingMethod, languageOfInstruction, modeOfDelivery**

**Ιmportant:** `getAdvancedCourses` doesn't always work properly due to lack of consistency of ICSD site. So it's better to use the `getBasicCourses` to retrieve basic course information.
