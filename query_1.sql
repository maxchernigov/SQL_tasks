SELECT student_id,name,AVG(grade.grade) as average_grade
FROM students
JOIN grade ON students.id = grade.student_id
GROUP BY student_id,students.name
ORDER BY average_grade DESC
LIMIT 5;