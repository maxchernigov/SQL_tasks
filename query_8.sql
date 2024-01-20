SELECT AVG(grade.grade) AS average_grade
FROM grade
JOIN subject ON grade.subject_id = subject.subject_id
JOIN teacher ON subject.teacher_id = teacher.teacher_id
WHERE teacher.teacher_name = 'Krystal Stark';