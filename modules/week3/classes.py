import random
import csv
import platform
import matplotlib as plt

class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        return (sum(grades) / len(grades)) 

    def etcs_progression(self):
        etcs = 0
        for e in self.data_sheet.courses:
            etcs += int(e.ETCS)
        return (etcs / 150) * 100

    def my_courses(self):
        return self.data_sheet.courses


class DataSheet():
    def __init__(self, courses=[]):
        self.courses = courses

    def get_grades_as_list(self):
        lst = []
        for c in self.courses:
            lst.append(c.grade)
        return lst



class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade




def get_students_from_csv():
    with open('modules/week3/students.csv') as f:
        reader = csv.reader(f)
        student_lst = []
        lst_courses = []
        count = 0

        for row in reader:
            lst_courses.append(Course(row[2],row[5],row[3],row[4],int(row[6])))
            count += 1
            if((count % 3) == 0):
                data_sheet = DataSheet(lst_courses)
                student = Student(row[0], row[1], data_sheet, row[7])
                student_lst.append(student)
                lst_courses = []         

           

        return student_lst;



def generate_students(n):
    c1 = Course('Functional Programming', 'Zoom-A', 'Anders', 15, 10)
    c2 = Course('JavaScript', 'Zoom-B', 'Lars', 20, 12)
    c3 = Course('Unity', 'Zoom-C', 'Arne', 10, 2)
    c4 = Course('Python', 'Zoom-D', 'Thomas', 5, 4)
    c5 = Course('Security', 'Zoom-E', 'Bjarne', 15, 7)

    names = ['Sven', 'Børge', 'Sofia', 'Lars', 'Michael', 'Maria', 'Sven2','Hanne', 'Henrik', 'Helene', 'Ulla', 'Anders']
    genders = ['Male', 'Female']
    courses = [c1, c2, c3, c4, c5]
    img_url = 'Img.png'
    students = []
    
    for idx, val in enumerate(range(0, n)):
        student_courses = []
        name = random.choice(names)
        gender = random.choice(genders)
        student_courses.append(random.choice(courses))
        student_courses.append(random.choice(courses))
        student_courses.append(random.choice(courses))
        data_sheet = DataSheet(student_courses)
        student = Student(name, gender, data_sheet, img_url)
        students.append(student)
    
    if platform.system() == 'Windows':
        newline=''
    else:
        newline = None
    

    with open('modules/week3/students.csv', 'w', newline=newline) as student_file:
        student_writer = csv.writer(student_file)
        for s in students:
            course1 = s.data_sheet.courses[0]
            course2 = s.data_sheet.courses[1]
            course3 = s.data_sheet.courses[2]
            student_writer.writerow([s.name, s.gender, course1.name, course1.teacher, course1.ETCS, course1.classroom, course1.grade, s.image_url])
            student_writer.writerow([s.name, s.gender, course2.name, course2.teacher, course2.ETCS, course2.classroom, course2.grade, s.image_url])
            student_writer.writerow([s.name, s.gender, course3.name, course3.teacher, course3.ETCS, course3.classroom, course3.grade, s.image_url])

