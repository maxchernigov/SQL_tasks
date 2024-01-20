SELECT students.name,grade.grade
FROM students
JOIN groups ON students.id = groups.group_id
JOIN grade ON students.id = grade.student_id
JOIN subject ON grade.subject_id = subject.subject_id
WHERE groups.name_group = 'Group-1' AND subject.subject_name = 'Subject-1';