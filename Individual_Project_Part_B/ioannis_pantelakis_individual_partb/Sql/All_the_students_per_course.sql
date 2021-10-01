Select projectpartb.courses.title,projectpartb.courses.language,projectpartb.courses.course_type,projectpartb.courses.description,
projectpartb.students.first_name,projectpartb.students.last_name
from projectpartb.courses
left join projectpartb.student_courses 
			inner join projectpartb.students
            on projectpartb.students.st_id = projectpartb.student_courses.st_id
on projectpartb.student_courses.c_id = projectpartb.courses.c_id 
order by projectpartb.courses.title asc;