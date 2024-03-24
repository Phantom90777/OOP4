class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка1'
g
    def average_score(self):
        return grade/len(grade)

    def __str__(self):
        return f"{self.name} {self.surname} {self.average_score} {self.finished_courses} {self.courses_in_progress}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"{self.name}!{self.surname}"
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_score(self):
        return grade/len(grade)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"{self.name}!{self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['JAWA']


best_student1 = Student('Ruoy', 'Eman', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['JAWA']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['JAWA']

cool_mentor1 = Reviewer('Some', 'Buddy')
cool_mentor1.courses_attached += ['Python']
cool_mentor1.courses_attached += ['JAWA']

test_lecturer = Lecturer('Ivan', 'Petrovich')
test_lecturer.courses_attached += ['Python']

test_lecturer1 = Lecturer('Ivan', 'Petrovich')
test_lecturer1.courses_attached += ['Python']

best_student.rate_hw(test_lecturer, 'Python', 7)

print(best_student)

# Знаю что задание не доделано. Возможно даже то что сделано - сделано криво. По другому не могу увы.
# Я и так купил платный курс на степике чтобы разобраться и сделать даже то, что выше написано.
# На большее не хватает ни сил ни терпения.