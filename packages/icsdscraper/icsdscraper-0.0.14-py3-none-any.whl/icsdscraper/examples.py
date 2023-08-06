import PapaScrap
import time
import icsd_objects

# TESTIN'

start_time = time.time()
    
# test professors
print('\n______________ Professors Test ______________')
professors = PapaScrap.getProfessors()

for obj in professors:
    print obj.name


# test basic courses
print('\n______________ Basic Courses Test ______________')
basic_courses = PapaScrap.getBasicCourses()

for obj in basic_courses:
    print obj.title


# test advanced courses
print('\n______________ Advanced Courses Test ______________')
#advanced_courses = PapaScrap.getAdvancedCourses()

#for obj in advanced_courses:
#    print obj.contentOutline


elapsed_time = time.time() - start_time

print("Elapsed Time:" + str(elapsed_time))


