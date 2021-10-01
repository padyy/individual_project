import random  #random library for use in dummy data

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
    
class Student_List(list): #student list class

    def PrintList(self):
        for student in self:
            print (Student)

    def lookupCourse(self,courseTitle): #search for a course for a student using the course title
        return [student for student in self if student.hasCourse(courseTitle)]

    def lookupMoreThanOne(self):
        return [student for student in self if student.hasMultipleCourses()]

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
    
    
class Trainer_List(list): #trainer list class

    def PrintList(self):
        for Trainer in self:
            print (Trainer)
            
    def lookupCourseT(self,courseTitle):
        return [trainer for trainer in self if trainer.hasCourse(courseTitle)]


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

class Assignment_List(list): #assignment list class

    def PrintList(self):
        for Assignment in self:
            print(Assignment)

    def lookupCourseA(self,courseTitle):
        return [assignment for assignment in self if assignment.hasCourse(courseTitle)]

class EmptyString: #class for empty input
    def __init__(self,string1):
        self.string1=string1
    
    def check_for_blank(self):
        return not(self.string1 and self.string1.strip())
