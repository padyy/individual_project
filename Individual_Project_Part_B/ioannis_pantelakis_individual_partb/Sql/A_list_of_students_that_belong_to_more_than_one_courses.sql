select projectpartb.students.first_name, projectpartb.students.last_name from students left join projectpartb.student_courses
	on projectpartb.students.st_id = projectpartb.student_courses.st_id
group by projectpartb.students.first_name
having count(projectpartb.student_courses.st_id) > 1 ;
