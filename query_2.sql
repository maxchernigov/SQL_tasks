SELECT student_id,name as studentss_name,AVG(grade.grade) AS average_grade
FROM students
JOIN grade ON students.id = grade.student_id
WHERE grade.subject_id = '4'
GROUP BY student_id,name
ORDER BY average_grade DESC
LIMIT 1;