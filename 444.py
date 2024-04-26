class Mentor:
    def __init__(self, name, surname, courses=[]):
        self.name = name
        self.surname = surname
        self.courses = courses


class Lecturer(Mentor):
    def __init__(self, name, surname, courses=[]):
        super().__init__(name, surname, courses)
        self.grades = {}

    def rate_lecture(self, student, course, grade):
        if course in self.courses:
            if course not in self.grades:
                self.grades[course] = []
            self.grades[course].append(grade)
            student.rate_lecture(course, grade)
        else:
            print(f"{self.name} {self.surname} is not teaching {course}.")


class Reviewer(Mentor):
    def rate_homework(self, student, course, grade):
        if course in self.courses:
            student.rate_homework(course, grade)
        else:
            print(f"{self.name} {self.surname} is not assigned to {course}.")


class Student:
    def __init__(self, name, surname, courses=[]):
        self.name = name
        self.surname = surname
        self.courses_in_progress = courses
        self.completed_courses = {}
        self.grades = {}

    def rate_homework(self, course, grade):
        if course in self.courses_in_progress:
            if course not in self.grades:
                self.grades[course] = []
            self.grades[course].append(grade)
        else:
            print(f"{self.name} {self.surname} is not studying {course}.")

    def rate_lecture(self, course, grade):
        if course in self.completed_courses:
            if course not in self.grades:
                self.grades[course] = []
            self.grades[course].append(grade)
        else:
            print(f"{self.name} {self.surname} has not completed {course} yet.")

    def __str__(self):
        completed_courses_str = ', '.join(self.completed_courses.keys())
        in_progress_courses_str = ', '.join(self.courses_in_progress)
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.average_grade('homework')}\n" \
               f"Курсы в процессе изучения: {in_progress_courses_str}\n" \
               f"Завершенные курсы: {completed_courses_str}"

    def average_grade(self, type_='homework'):
        if type_ == 'homework':
            grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        else:
            grades = [grade for course, grade in self.grades.items() if course in self.completed_courses]
        if grades:
            return sum(grades) / len(grades)
        else:
            return 0

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()


student1 = Student("Олег", "Олегов", ["Python", "Git"])
student2 = Student("Петр", "Петров", ["Python"])

lecturer1 = Lecturer("Алексей", "Алексеев", ["Python"])
lecturer2 = Lecturer("Михаил", "Михайлов", ["Git"])

reviewer1 = Reviewer("Елена", "Еленова", ["Python"])
reviewer2 = Reviewer("Ольга", "Ольгова", ["Git"])

print("---Выставление оценок---")
reviewer1.rate_homework(student1, "Python", 7)
reviewer1.rate_homework(student1, "Python", 10)
reviewer1.rate_homework(student2, "Python", 4)
reviewer2.rate_homework(student1, "Git", 6)
reviewer2.rate_homework(student2, "Git", 5)

lecturer1.rate_lecture(student1, "Python", 3)
lecturer1.rate_lecture(student2, "Python", 7)
lecturer2.rate_lecture(student1, "Git", 9)
lecturer2.rate_lecture(student2, "Git", 8)

print("---Вывод информации о каждом---")
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

def average_homework_grade(students, course):
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    return total_grade / count if count != 0 else 0

# Подсчет средней оценки за лекции всех лекторов в рамках курса
def average_lecture_grade(lecturers, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total_grade / count if count != 0 else 0

print("---Средняя оценка за домашние задания по курсу---")
print("Python:", average_homework_grade([student1, student2], "Python"))
print("Git:", average_homework_grade([student1, student2], "Git"))

print("---Средняя оценка за лекции по курсу---")
print("Python:", average_lecture_grade([lecturer1, lecturer2], "Python"))
print("Git:", average_lecture_grade([lecturer1, lecturer2], "Git"))