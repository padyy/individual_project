import random  #random library for use in dummy data
from db_handler import Db_handler

class Config: # class for auto input your info for the connection with db. 
    dbHost='localhost'
    dbUser='root'
    dbPassword='PadyPp2441990'
    dbName='projectpartb'

class Course:   #class for courses
    
    languages=['python','c#','java','javascript']
    types=["full time","part time"]
    
    def __init__(self,lang=None,course_type=None,title=None,description=None,auto=False):   #init for class of courses for with option for autofill data or for mannual
        if auto:
            self.lang=Course.languages[random.randint(0,len(Course.languages)-1)]
            self.course_type=Course.types[random.randint(0,len(Course.types)-1)]
            self.autotitle()
            self.description = self.title+': '+self.lang.capitalize()+' '+self.course_type
        else:
            self.lang=lang
            self.course_type=course_type
            self.title=title
            self.description = description
    
    def __str__(self):          #str for object print
        return (f'Title: {self.title}, Language: {self.lang.capitalize()}, Type: {self.course_type}, Description: {self.description}')

    def autotitle(self):
        self.title = ''
        langShort = ['py','c#','jv','js']
        self.title += langShort[Course.languages.index(self.lang)]
        if self.course_type == 'full time':
            self.title += 'Ft'
        elif self.course_type == 'part time':
            self.title += 'Pt'
        
        self.title += f'{random.randint(1,100):03d}'

    #Export from python and import to db the single course.
    def exportCourse(self):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f"INSERT INTO {dbh.dbName}.courses (language,course_type,title,description) VALUES ('{self.lang}', '{self.course_type}', '{self.title}', '{self.description}');")
            dbh.commit()
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex

    #Import to python from db single course with certain title
    def importCourse(self,title):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f"SELECT * FROM {dbh.dbName}.courses WHERE courses.title='{title}';")
            c_id, self.language, self.course_type, self.title, self.description = dbc.fetchone()
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex

#Course list class that extends the basic Python list
class Course_List(list):
    #Search for a course using the course title
    def courseLookup(self,courseTitle,courseLang):
        for course in self:
            if course.title==courseTitle and course.lang==courseLang:
                return course
        return None
    

    
    #Search List with the courses of certain lan
    def languageLookup(self,lang):
        return [course for course in self if course.lang == lang]

     #Append only if courseTitle not present, else raise exception with custom message
    def appendUnique(self,newcourse):
        for course in self:
            if course.title == newcourse.title:
                raise Exception('Course title is already in list!')
        self.append(newcourse)

    #Export from python and import to db the list with the courses.
    def exportCourseList(self):
        for course in self:
            course.exportCourse()

    #Import to python from db all courses 
    def importCourseList(self):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f"SELECT * FROM {dbh.dbName}.courses order by projectpartb.courses.title asc;")
            for row in dbc.fetchall():
                self.append(Course(lang=row[1],course_type=row[2],title=row[3],description=row[4]))
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex


from abc import ABC, abstractmethod

class SchoolMember(ABC):        #abstract class for blueprint for students and trainers.
    @abstractmethod
    def __init__(self,name,lastname,course):
        self.__name = name
        self.__lastname = lastname
        self.__course = course
    abstractmethod
    def __str__(self):
            return (f"SchoolMember's Name: {self.__name}, SchoolMember's Lastname: {self.__lastname} , SchoolMember's Course: {','.join(self.__course)}")

class Student(SchoolMember): #class for Student
    
    def __init__(self,name,lastname,courses,dob,fees):
        self.__name = name
        self.__lastname = lastname
        self.__courses = courses
        self.__dob = dob
        self.__fees = fees

    @property
    def name(self):
        return self.__name

    @property
    def lastname(self):
        return self.__lastname
      
    def __str__(self):
        return (f"Student's Name: {self.__name}, Student's Lastname: {self.__lastname}, Student's courses: {','.join(self.__courses)}, Student's date of bith: {self.__dob.strftime('%Y-%m-%d')}, Student's fees: {self.__fees}")    

    def hasCourse(self,courseTitle):  #search if student has course
        return courseTitle in self.__courses

    def hasMultipleCourses(self): #search if student have multiple courses
        return len(self.__courses) > 1

    #Export from python and import to db the single student.
    def exportStudent(self):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f"INSERT INTO {dbh.dbName}.students (first_name,last_name,birthdate,student_fees) VALUES ('{self.__name}', '{self.__lastname}', '{self.__dob}', {self.__fees});")
            dbh.commit()
            dbc.execute(f"SELECT st_id FROM {dbh.dbName}.students WHERE students.first_name='{self.__name}' AND students.last_name='{self.__lastname}';")
            st_id = dbc.fetchone()[0]
            for course in self.__courses:
                try:
                   # print(f"SELECT c_id FROM {dbh.dbName}.courses WHERE courses.title='{course}';")
                    dbc.execute(f"SELECT c_id FROM {dbh.dbName}.courses WHERE courses.title='{course}';")
                    c_id = dbc.fetchone()
                  #  print(c_id)
                    c_id = c_id[0]
                    dbc.execute(f"INSERT INTO {dbh.dbName}.student_courses (c_id,st_id) VALUES ({c_id}, {st_id});")
                    dbh.commit()
                except Exception as inEx:
                    print(inEx)
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex

    #Import to python from db single student with specific firstname and lastname
    def importStudent(self,firstname,lastname):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f"SELECT * FROM {dbh.dbName}.students WHERE students.first_name='{firstname}' AND students.last_name='{lastname}';")
            st_id, self.__name, self.__lastname, self.__dob, self.__fees = dbc.fetchone()
            dbc.execute(f"SELECT courses.title FROM {dbh.dbName}.student_courses JOIN {dbh.dbName}.courses ON student_courses.c_id=courses.c_id WHERE student_courses.st_id='{st_id}';")
            self.__courses = []
            for row in dbc.fetchall():
                self.__courses.append(row[0])
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex

    
class Student_List(list): #student list class

    def PrintList(self):
        for student in self:
            print (Student)

    def lookupCourse(self,courseTitle): #search for a course for a student using the course title
        return [student for student in self if student.hasCourse(courseTitle)]

    def lookupMoreThanOne(self):
        return [student for student in self if student.hasMultipleCourses()]

    #Export from python and import to db the list with the students.    
    def exportStudentList(self):
        for student in self:
            course.exportStudent()

    #Import to python from db all students
    def importStudentList(self):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f"SELECT * FROM {dbh.dbName}.students;")
            for row in dbc.fetchall():
                self.append(row)
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex
        
    #Import to python from db all student per course 
    def importStudentPerCourse(self):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f'Select {dbh.dbName}.courses.title,{dbh.dbName}.courses.language,{dbh.dbName}.courses.course_type,{dbh.dbName}.courses.description, '\
                        f'{dbh.dbName}.students.first_name,{dbh.dbName}.students.last_name from {dbh.dbName}.courses '\
                        f'left join {dbh.dbName}.student_courses inner join {dbh.dbName}.students on {dbh.dbName}.students.st_id = {dbh.dbName}.student_courses.st_id '\
                        f'on {dbh.dbName}.student_courses.c_id = {dbh.dbName}.courses.c_id order by {dbh.dbName}.courses.title asc;')
            for row in dbc.fetchall():
                self.append(row)
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex

    #Import to python from db all student that have more than one courses 
    def importStudentMoreThanOne(self):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f'select {dbh.dbName}.students.first_name, {dbh.dbName}.students.last_name from students left join {dbh.dbName}.student_courses '\
                        f'on {dbh.dbName}.students.st_id = {dbh.dbName}.student_courses.st_id '\
                        f'group by {dbh.dbName}.students.first_name '\
                        f'having count({dbh.dbName}.student_courses.st_id) > 1 ;')
            for row in dbc.fetchall():
                self.append(row)
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex
    

class Trainer(SchoolMember): #trainer class

    def __init__(self,name,lastname,subject,courses):
        self.__name = name
        self.__lastname = lastname
        self.__subject = subject
        self.__courses = courses

    def __str__(self):
        return (f"Trainer's Name: {self.__name}, Trainer's Lastname: {self.__lastname}, Trainer's subject: {self.__subject}, Trainer's courses: {','.join(self.__courses)}")
    
    def hasCourse(self,courseTitle):
        return courseTitle in self.__courses

    #Export from python and import to db the single trainer.
    def exportTrainer(self):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f"INSERT INTO {dbh.dbName}.trainers (first_name,last_name,trainer_subject) VALUES ('{self.__name}', '{self.__lastname}', '{self.__subject}');")
            dbh.commit()
            dbc.execute(f"SELECT tr_id FROM {dbh.dbName}.trainers WHERE trainers.first_name='{self.__name}' AND trainers.last_name='{self.__lastname}';")
            tr_id = dbc.fetchone()[0]
            for course in self.__courses:
                try:
                    dbc.execute(f"SELECT c_id FROM {dbh.dbName}.courses WHERE courses.title='{course}';")
                    c_id = dbc.fetchone()
                    c_id = c_id[0]
                    dbc.execute(f"INSERT INTO {dbh.dbName}.trainer_courses (c_id,tr_id) VALUES ({c_id}, {tr_id});")
                    dbh.commit()
                except Exception as inEx:
                    print(inEx)
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex

    #Import to python from db single trainer with specific firstname and lastname
    def importTrainer(self,firstname,lastname):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f"SELECT * FROM {dbh.dbName}.trainers WHERE trainers.first_name='{firstname}' AND trainers.last_name='{lastname}';")
            tr_id, self.__name, self.__lastname, self.__subject = dbc.fetchone()
            dbc.execute(f"SELECT courses.title FROM {dbh.dbName}.trainer_courses JOIN {dbh.dbName}.courses ON trainer_courses.c_id=courses.c_id WHERE trainer_courses.tr_id='{tr_id}';")
            self.__courses = []
            for row in dbc.fetchall():
                self.__courses.append(row[0])
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex
    
    
class Trainer_List(list): #trainer list class

    def PrintList(self):
        for Trainer in self:
            print (Trainer)
            
    def lookupCourseT(self,courseTitle):
        return [trainer for trainer in self if trainer.hasCourse(courseTitle)]

    #Export from python and import to db the list with the trainers.
    def exportTrainerList(self):
        for trainer in self:
            course.exportTrainer()

    #Import to python from db all trainers
    def importTrainerList(self):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f"SELECT * FROM {dbh.dbName}.trainers;")
            for row in dbc.fetchall():
                self.append(row)
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex
    #Import to python from db all trainers per course 
    def importTrainersPerCourse(self):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f'Select {dbh.dbName}.courses.title,{dbh.dbName}.courses.language,{dbh.dbName}.courses.course_type,{dbh.dbName}.courses.description, '\
                        f'{dbh.dbName}.trainers.first_name,{dbh.dbName}.trainers.last_name from {dbh.dbName}.courses '\
                        f'left join {dbh.dbName}.trainer_courses inner join {dbh.dbName}.trainers on {dbh.dbName}.trainers.tr_id = {dbh.dbName}.trainer_courses.tr_id '\
                        f'on {dbh.dbName}.trainer_courses.c_id = {dbh.dbName}.courses.c_id order by {dbh.dbName}.courses.title asc;')
            for row in dbc.fetchall():
                self.append(row)
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex

        
    
class Assignment: #assignment class

    def __init__(self,title,description,submission,acm,aom,courses):
        self.__title = title
        self._description = description
        self.__submission = submission
        self.__acm = acm
        self.__aom = aom
        self.__courses = courses

    def __str__(self):
        return(f"Assignment's title: {self.__title}, Assignment's description: {self._description}, Assigment's date of Submission: {self.__submission.strftime('%Y-%m-%d')},Assigment's code mark: {self.__acm}, Assigment's oral mark: {self.__aom}, Assigment's courses: {','.join(self.__courses)}")

    def hasCourse(self,courseTitle):
        return courseTitle in self.__courses

    #Export from python and import to db the single assignment.    
    def exportAssignment(self):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f"INSERT INTO {dbh.dbName}.assignments (as_title,as_descritpion,as_submission,acm,aom) VALUES ('{self.__title}', '{self._description}', '{self.__submission.strftime('%Y-%m-%d')}', '{self.__acm}', '{self.__aom}');")
            dbh.commit()
            dbc.execute(f"SELECT as_id FROM {dbh.dbName}.assignments WHERE assignments.as_title ='{self.__title}';")
            as_id = dbc.fetchone()[0]
            for course in self.__courses:
                try:
                    dbc.execute(f"SELECT c_id FROM {dbh.dbName}.courses WHERE courses.title='{course}';")
                    c_id = dbc.fetchone()
                    c_id = c_id[0]
                    dbc.execute(f"INSERT INTO {dbh.dbName}.course_assignments (c_id,as_id) VALUES ({c_id}, {as_id});")
                    dbh.commit()
                except Exception as inEx:
                    print(inEx)
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex

    #Import to python from db single assignment with certain title        
    def importAssignment(self,title):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f"SELECT * FROM {dbh.dbName}.assignments WHERE assignments.title='{title}';")
            as_id, self.__title, self._description, self.__acm, self.__aom  = dbc.fetchone()
            dbc.execute(f"SELECT courses.title FROM {dbh.dbName}.course_assignments JOIN {dbh.dbName}.courses ON course_assignments.c_id=courses.c_id WHERE course_assignments.as_id='{as_id}';")
            self.__courses = []
            for row in dbc.fetchall():
                self.__courses.append(row[0])
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex

class Assignment_List(list): #assignment list class

    def PrintList(self):
        for Assignment in self:
            print(Assignment)

    def lookupCourseA(self,courseTitle):
        return [assignment for assignment in self if assignment.hasCourse(courseTitle)]

    #Export from python and import to db the list with the assignments.
    def exportAssignmentList(self):
        for assignment in self:
            course.exportAssignment()

    #Import to python from db all assignments            
    def importAssignmentList(self):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f"SELECT * FROM {dbh.dbName}.assignments;")
            for row in dbc.fetchall():
                self.append(row)
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex

    #Import to python from db all assignments per course    
    def importAssignmentsPerCourse(self):
        dbh = Db_handler(host=Config.dbHost,user=Config.dbUser,password=Config.dbPassword,dbName=Config.dbName)
        dbh.connect()
        dbc = dbh.getCursor()
        try:
            dbc.execute(f'Select {dbh.dbName}.courses.title,{dbh.dbName}.courses.language,{dbh.dbName}.courses.course_type,{dbh.dbName}.courses.description, '\
                        f'{dbh.dbName}.assignments.as_title ,{dbh.dbName}.assignments.as_descritpion from {dbh.dbName}.courses '\
                        f'left join {dbh.dbName}.course_assignments inner join {dbh.dbName}.assignments on {dbh.dbName}.assignments.as_id = {dbh.dbName}.course_assignments.as_id '\
                        f'on {dbh.dbName}.course_assignments.c_id = {dbh.dbName}.courses.c_id order by {dbh.dbName}.courses.title asc;')
            for row in dbc.fetchall():
                self.append(row)
            dbh.disconnect()
            return None
        except Exception as ex:
            dbh.disconnect()
            return ex

        
class EmptyString: #class for empty input
    def __init__(self,string1):
        self.string1=string1
    
    def check_for_blank(self):
        return not(self.string1 and self.string1.strip())




