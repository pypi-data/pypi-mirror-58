
class Professor(object):
        def __init__(self, name, rank, link, office, tel, email, website, image_link):
                self.name = name
                self.rank = rank
                self.link = link
                self.office = office
                self.tel = tel
                self.email = email
                self.website = website
                self.image_link = image_link

class BasicCourse(object):
        def __init__(self, title, code, semester, ects, theoryHours, labHours, professor, link):
                self.title = title
                self.code = code
                self.semester = semester
                self.ects = ects
                self.theoryHours = theoryHours
                self.labHours = labHours
                self.professor = professor
                self.link = link

class AdvancedCourse(object):
        def __init__(self, contentOutline, learningOutcomes, prerequisites, basicTextbooks, additionalReferences, teachingMethod, grandingMethod, languageOfInstruction, modeOfDelivery):
                self.contentOutline = contentOutline
                self.learningOutcomes = learningOutcomes
                self.prerequisites = prerequisites
                self.basicTextbooks = basicTextbooks
                self.additionalReferences = additionalReferences
                self.teachingMethod = teachingMethod
                self.grandingMethod = grandingMethod
                self.languageOfInstruction = languageOfInstruction
                self.modeOfDelivery = modeOfDelivery
