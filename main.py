import psycopg2
from faker import Faker
import random
import json

# Установка соединения с базой данных
conn = psycopg2.connect(host="localhost", database="postgres", user="postgres")
cur = conn.cursor()

# Инициализация Faker
fake = Faker()


# Определение функции to_json
def to_json(data, filename="output.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Data were saved to {filename}.")


def create_groups(groups_list, n=3):
    for i in range(1, n + 1):
        group = {"group_id": i, "group_name": f"Group-{i}"}
        groups_list.append(group)


def create_subjects(subjects_list, n=8):
    for i in range(1, n + 1):
        subject = {"subject_id": i, "subject_name": f"Subject-{i}"}
        subjects_list.append(subject)


def create_teachers(teachers_list, n=5):
    for i in range(1, n + 1):
        teacher = {"teacher_id": i, "teacher_name": fake.name()}
        teachers_list.append(teacher)


def create_grades(grades_list, students_count=30, subjects_count=8):
    for student_id in range(1, students_count + 1):
        for subject_id in range(1, subjects_count + 1):
            grade = {
                "student_id": student_id,
                "subject_id": subject_id,
                "grade": random.randint(1, 10),
            }
            grades_list.append(grade)


def create_students(students_list, n=30):
    for i in range(1, n + 1):
        student = {"student_id": i, "name": fake.name(), "age": random.randint(18, 25)}
        students_list.append(student)


# Создание данных для групп, предметов, викладачів та оцінок
groups = []
create_groups(groups)
to_json(groups, filename="groups.json")

subjects = []
create_subjects(subjects)
to_json(subjects, filename="subjects.json")

teachers = []
create_teachers(teachers)
to_json(teachers, filename="teachers.json")

students = []
create_students(students)
to_json(students, filename="students.json")

grades = []
create_grades(grades, students_count=len(students))
to_json(grades, filename="grades.json")

# Вставка данных в таблицы базы данных
for group in groups:
    cur.execute(
        "INSERT INTO groups (group_id, name_group) VALUES (%s, %s)",
        (group["group_id"], group["group_name"]),
    )

for subject in subjects:
    cur.execute(
        "INSERT INTO subject (subject_id, subject_name,teacher_id) VALUES (%s, %s,%s)",
        (subject["subject_id"], subject["subject_name"], subject["teacher_id"]),
    )

for teacher in teachers:
    cur.execute(
        "INSERT INTO teacher(teacher_id, teacher_name) VALUES (%s, %s)",
        (teacher["teacher_id"], teacher["teacher_name"]),
    )

for student in students:
    cur.execute(
        "INSERT INTO students (id, name, age) VALUES (%s, %s, %s)",
        (student["student_id"], student["name"], student["age"]),
    )

for grade in grades:
    cur.execute(
        "INSERT INTO grade (student_id, subject_id, grade) VALUES (%s, %s, %s)",
        (grade["student_id"], grade["subject_id"], grade["grade"]),
    )

# Фиксация изменений и закрытие соединения
conn.commit()
cur.close()
conn.close()
