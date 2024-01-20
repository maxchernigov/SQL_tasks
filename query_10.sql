SELECT DISTINCT subject.subject_name
FROM students
JOIN groups ON students.id = groups.group_id
JOIN grade ON students.id = grade.student_id
JOIN subject ON grade.subject_id = subject.subject_id
JOIN teacher ON subject.teacher_id = teacher.teacher_id
WHERE students.id = 1 AND teacher.teacher_id = 2;