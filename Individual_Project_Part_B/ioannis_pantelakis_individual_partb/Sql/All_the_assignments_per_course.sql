Select projectpartb.courses.title,projectpartb.courses.language,projectpartb.courses.course_type,projectpartb.courses.description,
projectpartb.assignments.as_title ,projectpartb.assignments.as_descritpion
from projectpartb.courses
left join projectpartb.course_assignments 
			inner join projectpartb.assignments
            on projectpartb.assignments.as_id = projectpartb.course_assignments.as_id
on projectpartb.course_assignments.c_id = projectpartb.courses.c_id 
order by projectpartb.courses.title asc;
