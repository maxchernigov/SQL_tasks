SELECT students.name
FROM students
JOIN groups ON students.id = groups.group_id
WHERE groups.name_group = 'Group-1';