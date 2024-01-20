SELECT DISTINCT subject.subject_name
FROM teacher
JOIN subject ON teacher.teacher_id = subject.teacher_id
WHERE subject.teacher_id = 2;