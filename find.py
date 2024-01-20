import psycopg2

conn = psycopg2.connect(host="localhost", database="postgres", user="postgres")
cur = conn.cursor()

# request №1
cur.execute(
    """
SELECT student_id,name,AVG(grade.grade) as average_grade
FROM students
JOIN grade ON students.id = grade.student_id
GROUP BY student_id,students.name
ORDER BY average_grade DESC
LIMIT 5;
"""
)
result1 = cur.fetchall()
print("Top 5 students with highest average grades:", result1)

# request №2
subject_id = 1
cur.execute(
    """
SELECT student_id,name as studentss_name,AVG(grade.grade) AS average_grade
FROM students
JOIN grade ON students.id = grade.student_id
WHERE grade.subject_id = '4'
GROUP BY student_id,name
ORDER BY average_grade DESC
LIMIT 1;
"""
)
result2 = cur.fetchone()
print(f"Student with highest average grade in Subject-{subject_id}:", result2)

# request №3
cur.execute(
    """
SELECT groups.name_group, AVG(grade.grade) as average_grade
FROM students
JOIN groups ON students.id = groups.group_id 
JOIN grade ON students.id = grade.student_id
WHERE grade.subject_id = 2
GROUP BY groups.name_group;
"""
)

# request №4
cur.execute(
    """
SELECT AVG(grade) AS average_grade
FROM grade;

"""
)

# request №5
cur.execute(
    """
SELECT DISTINCT subject.subject_name
FROM teachers
JOIN subject ON teacher.teacher_id = subject.teacher_id
WHERE teacher.teacher_id = 3;

"""
)

# request №6
cur.execute(
    """
SELECT students.name
FROM students
JOIN groups ON students.id = groups.group_id
WHERE groups.name_group = 'Group-1';

"""
)

# request №7
cur.execute(
    """
SELECT students.name,grade.grade
FROM students
JOIN groups ON students.id = groups.group_id
JOIN grade ON students.id = grade.student_id
JOIN subject ON grade.subject_id = subject.subject_id
WHERE groups.name_group = 'Group-1' AND subject.subject_name = 'Subject-1';
"""
)

# request №8
cur.execute(
    """
SELECT AVG(grade.grade) AS average_grade
FROM grade
JOIN subject ON grade.subject_id = subject.subject_id
JOIN teacher ON subject.teacher_id = teacher.teacher_id
WHERE teacher.teacher_name = 'Krystal Stark';
"""
)

# request №9
cur.execute(
    """
SELECT subject.subject_name
FROM subject
JOIN subject ON grade.subject_id = subject.subject_id
WHERE grade.student_id = 1;
"""
)

# request №10
cur.execute(
    """
SELECT subject.subject_name
FROM grade
JOIN subject ON grade.subject_id = subject.subject_id
JOIN teacher ON subject.teacher_id = teacher.teacher_id
WHERE grade.student_id = 1 AND teacher.teacher_name = 'Krystal Stark';
"""
)

conn.commit()
cur.close()
conn.close()
