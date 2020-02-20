class Student():
    def __init__(self, name, gender, datasheet, image_url):
        self.name = name
        self.gender = gender
        self.datasheet = datasheet
        self.image_url = image_url

class Course():
    def __init__(self, name, teacher, ETCS, classroom, grade='0'):
        self.name = name
        self.teacher = teacher
        self.ETCS = ETCS
        self.classroom = classroom
        self.grade = grade
    def returnContent(self):
        return self.name, self.teacher, self.ETCS, self.classroom

class DataSheet():
    def __init__(self, courses):
        self.courses = courses
