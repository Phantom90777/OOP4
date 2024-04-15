class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_scores = {}

    def __str__(self):
        return f"{super().__str__()}\nСредняя оценка за лекции: {self.calculate_average_score():.1f}"

    def calculate_average_score(self):
        if not self.lecture_scores:
            return 0
        total_score = sum(sum(scores) for scores in self.lecture_scores.values())
        total_lectures = sum(len(scores) for scores in self.lecture_scores.values())
        return total_score / total_lectures


class Reviewer(Mentor):
    def __str__(self):
        return super().__str__()


def rate_lecturer(lecturer, course, score):
    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
        if course in lecturer.lecture_scores:
            lecturer.lecture_scores[course].append(score)
        else:
            lecturer.lecture_scores[course] = [score]


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.completed_courses = {}
        self.homework_scores = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.calculate_average_score():.1f}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.completed_courses.keys())}"

    def calculate_average_score(self):
        if not self.homework_scores:
            return 0
        total_score = sum(sum(scores) for scores in self.homework_scores.values())
        total_assignments = sum(len(scores) for scores in self.homework_scores.values())
        return total_score / total_assignments


# Создание экземпляров классов
student1 = Student("Иван", "Иванов")
student2 = Student("Петр", "Петров")
lecturer1 = Lecturer("Алексей", "Алексеев")
lecturer2 = Lecturer("Михаил", "Михайлов")
reviewer1 = Reviewer("Елена", "Еленова")
reviewer2 = Reviewer("Ольга", "Ольгова")

# Проверка методов
print("--- Информация о студентах ---")
print(student1)
print("\n--- Информация о лекторах ---")
print(lecturer1)
print("\n--- Информация о проверяющих ---")
print(reviewer1)

# Добавление курсов преподавателям и студентам
lecturer1.courses_attached.append("Python")
lecturer2.courses_attached.append("JavaScript")
reviewer1.courses_attached.append("Python")
reviewer2.courses_attached.append("JavaScript")
student1.courses_in_progress.append("Python")
student2.courses_in_progress.append("JavaScript")

# Выставление оценок студентам и лекторам
rate_lecturer(lecturer1, "Python", 8)
rate_lecturer(lecturer1, "Python", 9)
rate_lecturer(lecturer2, "JavaScript", 7)
rate_lecturer(lecturer2, "JavaScript", 10)

# Проверка выставленных оценок
print("\n--- Проверка выставленных оценок ---")
print(f"Оценки лектора 1 за курс Python: {lecturer1.lecture_scores}")
print(f"Оценки лектора 2 за курс JavaScript: {lecturer2.lecture_scores}")


# Реализация функций подсчета средней оценки
def calculate_average_homework_score(students, course):
    total_score = sum(
        sum(scores) for student in students for key, scores in student.homework_scores.items() if key == course)

    total_assignments = sum(
        len(scores) for student in students for key, scores in student.homework_scores.items() if key == course)
    return total_score / total_assignments if total_assignments > 0 else 0


def calculate_average_lecture_score(lecturers, course):
    total_score = sum(sum(scores) for lecturer in lecturers for key, scores in lecturer.lecture_scores.items() if key == course)
    total_lectures = sum(
        len(scores) for lecturer in lecturers for key, scores in lecturer.lecture_scores.items() if key == course)
    return total_score / total_lectures if total_lectures > 0 else 0


# Проверка функций подсчета средней оценки
print("\n--- Проверка функций подсчета средней оценки ---")
print(
    f"Средняя оценка за домашние задания по курсу Python: {calculate_average_homework_score([student1, student2], 'Python'):.1f}")
print(
    f"Средняя оценка за лекции по курсу JavaScript: {calculate_average_lecture_score([lecturer1, lecturer2], 'JavaScript'):.1f}")
