import random
import matplotlib.pyplot as plt

#Ex 1 Classes

#1.-6.
class Student():
    def __init__(self, name, gender, datasheet, image_url):
        self.name = name
        self.gender = gender
        self.datasheet = datasheet
        self.image_url = image_url
        self.grade = None
        
    def setAvgGrade(self, grade):
        self.grade = grade
    def getAvgGrade(self):
        return self.grade
        
    def getName(self):
        return self.name
    def getGender(self):
        return self.gender
    def getData(self):
        return self.datasheet
    def getImage(self):
        return self.image_url
     
    def get_avg_grade(self):
        #print('avg funktionen')
        grades = self.datasheet.get_grades_as_list()  
        all_grades = 0
        for grade in grades:
            if grade:
                all_grades += grade
            else:
                continue
        if len(grades) != 0:
            avg_grade = all_grades/len(grades)
        else:
            return 0
        return avg_grade
    
    def get_ETCS(self):
        ETCS = self.datasheet.get_ETC_as_list()
        all_ETCS = 0
        for ETC in ETCS:
            all_ETCS += ETC
        progression = all_ETCS/150
        return progression * 100
        
        #done = progression * 100
        #return str(done) + '% fuldført'
        

class Course():
    haveGrade = False
    
    def __init__(self, name, teacher, ETCS, classroom, grade=None): #grade=None
        self.name = name
        self.teacher = teacher
        self.ETCS = ETCS
        self.classroom = classroom
             
        if grade:
            self.grade = grade
            self.haveGrade = True
    
    def getName(self):
        return self.name
    def getTeacher(self):
        return self.teacher
    def getETCS(self):
        return self.ETCS
    def getClassroom(self):
        return self.classroom
    
    def getGrade(self):
        if self.haveGrade == True:
            return self.grade
        
    
    def returnContent(self):
        return self.name, self.gender, self.teacher, self.ETCS, self.classroom, self.image_url

class DataSheet(): #denne kan godt checke for null
    def __init__(self, courses): #*courses
        self.courses = courses
    
    def getCourses(self):
        return self.courses
    
    def get_grades_as_list(self):
        #print('get grades as list funktion')
        grades = []
        for course in self.courses:
            if hasattr(course, 'grade'):
                grades.append(course.grade)
            else:
                continue 
        return grades
    
    def get_ETC_as_list(self):
        ETC_points = []
        for course in self.courses:
            ETC_points.append(course.ETCS)
        return ETC_points


#7.
def generateStudents(n):
    names = ['Mummi', 'Bubber', 'Tjasse', 'Saxa', 'Odin', 'Asger']
    image_urls = ['https://bit.ly/2xRStOw', 'https://bit.ly/2V40lnS', 'https://bit.ly/2V1kuuQ', 'https://bit.ly/3dY9Cqj']
    gender = ['f', 'm']
    
    students = []
    
    for i in range(0, n):
        data = generateCoursesAndData()
        students.append(Student(random.choice(names), random.choice(gender), data, random.choice(image_urls)))
    
    return students 

def writeStudentsToFile(filename, n):
    student_list = generateStudents(n)
    with open(filename, 'a') as studentFile:
        for student in student_list:
            studentFile.write('Name of student: ')
            studentFile.write(student.getName())
            studentFile.write('\n')
            studentFile.write('Gender of student: ')
            studentFile.write(student.getGender())
            studentFile.write('\n')
            studentFile.write('Student image url: ')
            studentFile.write(student.getImage())
            studentFile.write('\n')
            studentFile.write('\n')
            
            studentFile.write('Course 1: ')
            studentFile.write(student.getData().getCourses()[0].getName())
            studentFile.write('\n')
            studentFile.write('Classroom: ')
            studentFile.write(str(student.getData().getCourses()[0].getClassroom()))
            studentFile.write('\n')
            studentFile.write('Teacher: ')
            studentFile.write(student.getData().getCourses()[0].getTeacher())
            studentFile.write('\n')
            studentFile.write('Grade: ')
            studentFile.write(str(student.getData().getCourses()[0].getGrade()))
            studentFile.write('\n')
            studentFile.write('\n')
                      
            studentFile.write('Course 2: ')
            studentFile.write(student.getData().getCourses()[1].getName())
            studentFile.write('\n')
            studentFile.write('Classroom: ')
            studentFile.write(str(student.getData().getCourses()[1].getClassroom()))
            studentFile.write('\n')
            studentFile.write('Teacher: ')
            studentFile.write(student.getData().getCourses()[1].getTeacher())
            studentFile.write('\n')
            studentFile.write('Grade: ')
            studentFile.write(str(student.getData().getCourses()[1].getGrade()))
            studentFile.write('\n')
            studentFile.write('\n')
                      
            studentFile.write('Course 3: ')
            studentFile.write(student.getData().getCourses()[2].getName())
            studentFile.write('\n')
            studentFile.write('Classroom: ')
            studentFile.write(str(student.getData().getCourses()[2].getClassroom()))
            studentFile.write('\n')
            studentFile.write('Teacher: ')
            studentFile.write(student.getData().getCourses()[2].getTeacher())
            studentFile.write('\n')
            studentFile.write('Grade: ')
            studentFile.write(str(student.getData().getCourses()[2].getGrade()))
            studentFile.write('\n')
            studentFile.write('\n')
            studentFile.write('\n')
            studentFile.write('\n')


#8.
def getStudentsAnd(file):
    with open(file) as file_object:
        lines = file_object.readlines()
    
    students = []
    
    n = 0
    
    for i in range(0, len(lines), 5):
        students.append(Student(lines[i][6:-1], lines[i+1][8:-1] , 'data', lines[i+2][9:-1]))
        students[n].setAvgGrade(lines[i+3][11:-1])
        n = n + 1
    #return students
    
    for x in range(0, len(students)):
        print(students[x].getName())
        print(students[x].getGender())
        print(students[x].getImage())
        print(students[x].getAvgGrade())

    
    gradeList = sorted(students, key=lambda x: x.grade, reverse=True)
    grades = [i.grade for i in gradeList]
    names = [i.name for i in gradeList]

    plt.bar(names, grades)
    plt.axis([0, 5, 0, 5])
    plt.figure(figsize=(5, 10))


def generateCoursesAndData():
    names = ['Physics', 'History', 'PE', 'Danish', 'English', 'German']
    teachers = ['Freja', 'Frig', 'Frej', 'Njord', 'Mimer']
    grades = [-3, 0, 2, 4, 7, 10, 12, None] #er det denne der giver fejlen?
    ETCS = [10, 5, 20, 15, 25, 30]
    class_rooms = ['101', '202', '303', '401', '505', '609']
    
    courseList = []
    
    for i in range(0, 3):  
        courseList.append(Course(random.choice(names), random.choice(teachers), random.choice(ETCS), random.choice(class_rooms), random.choice(grades)))
    
    return DataSheet(courseList)
    

