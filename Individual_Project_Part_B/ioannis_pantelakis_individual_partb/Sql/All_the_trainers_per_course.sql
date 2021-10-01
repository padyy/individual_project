Select projectpartb.courses.title,projectpartb.courses.language,projectpartb.courses.course_type,projectpartb.courses.description,
projectpartb.trainers.first_name,projectpartb.trainers.last_name
from projectpartb.courses
left join projectpartb.trainer_courses 
			inner join projectpartb.trainers
            on projectpartb.trainers.tr_id = projectpartb.trainer_courses.tr_id
on projectpartb.trainer_courses.c_id = projectpartb.courses.c_id  
order by projectpartb.courses.title asc;