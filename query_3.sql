SELECT groups.name_group, AVG(grade.grade) as average_grade
FROM students
JOIN groups ON students.id = groups.group_id 
JOIN grade ON students.id = grade.student_id
WHERE grade.subject_id = 2
GROUP BY groups.name_group;