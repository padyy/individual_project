''' Coding Bootcamp - Individual Project Brief.
-Title:  Design of a Private School Structure
-Last name : Pantelakis
-First Name: Ioannis
-Advisor: Tyrovola Sarantia
-Python ver:3.9.2
-win: win10 64bit                           '''


import datetime #import labriary of datetime for using in date of birth format-validation

def grammes(number_of_lines): ##function for design of menu with lines
    
    draw=' '
    for i in range(number_of_lines):
        draw+="-"
    return draw

def course_func(courses): ##fuction for courses inputs
    
     languages={'python','c#','java','javascript'}
     types={"full time","part time"}
     flag=False
     dec1='Y'
     print('Please give the info about the courses.\n')
     while True:
                if flag:
                    while True:                                                                                       #Check for another Course
                        dec1 = input("Want to add another course? Type 'y' for yes and 'n' for no.")
                        dec1=dec1.upper()
                        if dec1=='Y' or dec1=='N':
                            break
                        else:
                            print("Wrong input..")
                            
                i = 1
                
                if dec1 == 'Y':
                    while i<5:                                                                                        #Check for Course's language
                        if i == 1:
                            print("Course's availabe Languages: Python,C#,Java,JavaScript.")
                            while True:
                                c_l = input("Give Course's Language: ")
                                c_l = c_l.lower()
                                if c_l not in languages:
                                    print('Wrong language.Please give one of the above: Python,C#,Java,JavaScript')
                                else:
                                    break
                            if c_l == 'python':
                                course_language='Python'
                            elif c_l == 'c#':
                                course_language='C#'
                            elif c_l == 'java':
                                course_language='Java'
                            else:
                                course_language = 'JavaScript'
                                
                        elif i == 2:
                            
                            courses_title=input("Give Course's Title : ")                                            #Check for Course's title
                        
                            
                            while courses_title in courses[course_language]:                                         #Check for diplicates in titles                     
                                print('Title already exists. Please give a unique title.')
                                courses_title=input("Give Course's Title : ")
                                
                        elif i == 3:
                            course_description=input("Give Course's Description: ")                                 #Check for Course's description
                            
                        else:
                            print("Course's availabe types: Full time,Part time")
                            
                            while True:
                                course_type=input("Give Course's Type: ")
                                course_type = course_type.lower()
                                if course_type not in types:
                                    print('Wrong type.Please give one of the above: Full time,Part time')
                                else:
                                    break
                            
                            
                        i = i+1
                
                    
                    flag=True
                    courses[course_language][courses_title]={'description':course_description,'type':course_type}   #Courses dictionary fill with the info
                else:
                    break

     return courses

def Trainers_func(trainers,courses): ##fuction for trainer inputs
    languages = {'python','c#','java','javascript'}
    flag_add_trainer=0
    flag = False
    dec1 = 'Y'
    dec2 = 'Y'
    dec3 = 'Y'
    flagg = 0
    print('Please give the info about the Trainers.\n')
    while True:
            if flag_add_trainer:    #decision for add more trainers                                                                       
                while True:
                    dec1 = input("Want to add another trainer? Type 'y' for yes and 'n' for no.")
                    dec1=dec1.upper()
                    if dec1 == 'Y' or dec1 == 'N':
                        dec3 = 'Y'
                        dec2 = 'Y'
                        flag = False
                        flag_add_trainer = 0
                        break
                    else:
                        print("Wrong input..")
                    
                    
            trainer_courses = []
            if dec1 == 'Y':     #Trainer info input  
                trainer_firstname = input("Give Trainer's first name: ")            
                trainer_lastname = input("Give Trainer's last name: ")
                trainer_subject = input("Give Trainer's subject: ")
                flag2=False
                while True:
                    if flag2:
                        while True:    #decision for another language for trainer
                            dec3 = input("Want to add another language for the trainer? Type 'y' for yes and 'n' for no.")
                            dec2='Y'
                            flag = 0
                            dec3 = dec3.upper()
                            if dec3 == 'Y' or dec3 == 'N':
                                 break
                            else:
                                print("Wrong input..")
                    if dec3 == 'Y':
                        emptylist = 1
                        while  emptylist:  ##input for trainer's course language. With that i can have synchronization with the courses dict.  
                            print("Choose Trainer's language from the following language's list:\n ( Python,C#,Java,JavaScript.)")
                            while True:
                                t_l = input("Please input the trainer's Language: ")
                                t_l = t_l.lower()
                                if t_l not in languages:
                                    print('Wrong language.Please give one of the above: Python,C#,Java,JavaScript')
                                else:
                                    break
                            if t_l == 'python':
                                 course_language1='Python'
                            elif t_l == 'c#':
                                 course_language1='C#'
                            elif t_l == 'java':
                                course_language1='Java'
                            else:
                                course_language1 = 'JavaScript'
                        
                            if  courses[course_language1]:
                                emptylist = 0
                            if emptylist != 0:
                                print('List of courses for this Language is Empty. Please choose another language')
                            
                        while True:  ##input for trainers course title that depend on language.
                            if dec2 == 'Y':
                                flagg = 0
                                while not flag:
                                    print('Please choose a course title for the trainer, from the list above:')
                                    
                                    for courseTitle in courses[course_language1]:
                                       print(f'{courseTitle},',end='')
                                    trainer_courses_input=input('\nPlease input the title: ')
                                    for courseTitle in courses[course_language1]:
                                        if trainer_courses_input == courseTitle:
                                            
                                            flagg = 1
                                    if flagg==1:
                                        trainer_courses.append(trainer_courses_input)
                                        flag = 1
                                    else:
                                        print('Wrong Input.Please try again.')
                                          
                                while True:   #decision for another course title for trainer
                                    dec2 = input("Want to add another course_title for the trainer? Type 'y' for yes and 'n' for no :")
                                    dec2 = dec2.upper()
                        
                                    if dec2 == 'Y':
                                        
                                        flag = 0
                                        break
                                        
                                    elif dec2 == 'N':
                                        
                                        break
                                    else:
                                        print("Wrong input..")
                                    
                                        
                            else:
                                 break
                            flag2 = True           
                    else:
                        break
                    flag_add_trainer = True     #Above this line trainers dictionary fill with the info
                    trainers[trainer_firstname+'_'+trainer_lastname] = {'name':trainer_firstname,'surname':trainer_lastname,'specialty':trainer_subject,'courses':trainer_courses}
            else:
                break
    return trainers


def Students_func(students,courses): ##fuction for Students inputs
    languages = {'python','c#','java','javascript'}
    flag_add_student=0
    flag = False
    dec1 = 'Y'
    dec2 = 'Y'
    dec3 = 'Y'
    flagg = 0
    print('Please give the info about the Students.\n')
    while True:
            if flag_add_student:    #decision for add more students                                                                       
                while True:
                    dec1 = input("Want to add another student? Type 'y' for yes and 'n' for no.")
                    dec1=dec1.upper()
                    if dec1 == 'Y' or dec1 == 'N':
                        dec3 = 'Y'
                        dec2 = 'Y'
                        flag = False
                        flag_add_student = 0
                        break
                    else:
                        print("Wrong input..")
                    
                    
            student_courses = []
            if dec1 == 'Y':     #Student info input  
                student_firstname = input("Give Student's first name: ")            
                student_lastname = input("Give Student's last name: ")
                print('Give date of birth using the following format : YYYY-MM-DD')
                date_format="%Y-%m-%d"
                while True:
                    try:
                        student_birth = input('Please give the date: ')
                        datetime.datetime.strptime(student_birth, date_format)   
                    except ValueError:
                        print("This is the incorrect date string format.It should be YYYY-MM-DD")
                    else:
                        print("This is the correct date format. Input successfull.")
                        break

                while True:
                    try:
                        student_fees =float(input("Give Student's tuition fees: "))
                    except ValueError:
                        print('Wrong data type, please give a float number.')
                    else:
                        break
                        
                flag2=False
                while True:
                    if flag2:
                        while True:    #decision for another language for student

                            dec3 = input("Want to add another language for the student? Type 'y' for yes and 'n' for no.")
                            dec2='Y'
                            flag = 0
                            dec3 = dec3.upper()
                            if dec3 == 'Y' or dec3 == 'N':
                                 break
                            else:
                                print("Wrong input..")
                    if dec3 == 'Y':
                        emptylist = 1
                        while  emptylist:  ##input for student's course language. With that i can have synchronization with the courses dict.  
                            print("Choose Student's language from the following language's list:\n ( Python,C#,Java,JavaScript.)")
                            while True:
                                t_l = input("Please input the student's Language: ")
                                t_l = t_l.lower()
                                if t_l not in languages:
                                    print('Wrong language.Please give one of the above: Python,C#,Java,JavaScript')
                                else:
                                    break
                            if t_l == 'python':
                                 course_language1='Python'
                            elif t_l == 'c#':
                                 course_language1='C#'
                            elif t_l == 'java':
                                course_language1='Java'
                            else:
                                course_language1 = 'JavaScript'
                        
                            if  courses[course_language1]:
                                emptylist = 0
                            if emptylist != 0:
                                print('List of courses for this Language is Empty. Please choose another language')
                            
                        while True:  ##input for students course title that depend on language.
                            if dec2 == 'Y':
                                flagg = 0
                                while not flag:
                                    print('Please choose a course title for the student, from the list above:')
                                    
                                    for courseTitle in courses[course_language1]:
                                       print(f'{courseTitle},',end='')
                                    student_courses_input=input('\nPlease input the title: ')
                                    for courseTitle in courses[course_language1]:
                                        if student_courses_input == courseTitle:
                                            
                                            flagg = 1
                                    if flagg==1:
                                        student_courses.append(student_courses_input)
                                        flag = 1
                                    else:
                                        print('Wrong Input.Please try again.')
                                          
                                while True:   #decision for another course title for student
                                    dec2 = input("Want to add another course_title for the student? Type 'y' for yes and 'n' for no :")
                                    dec2 = dec2.upper()
                        
                                    if dec2 == 'Y':
                                        
                                        flag = 0
                                        break
                                        
                                    elif dec2 == 'N':
                                        
                                        break
                                    else:
                                        print("Wrong input..")
                                    
                                        
                            else:
                                 break
                            flag2 = True           
                    else:
                        break
                    flag_add_student = True     #Above this line students dictionary fill with the info
                    students[student_firstname+'_'+student_lastname] = {'name':student_firstname,'surname':student_lastname,'dob':student_birth,'tf':student_fees,'courses':student_courses}
            else:
                break
    return students    
   

def Assignments_func(assignments,courses): ##fuction for Assignments inputs
    languages = {'python','c#','java','javascript'}
    flag_add_assignment=0
    flag = False
    dec1 = 'Y'
    dec2 = 'Y'
    dec3 = 'Y'
    flagg = 0
    print('Please give the info about the Assignments.\n')
    while True:
            if flag_add_assignment:    #decision for add more assignments                                                                       
                while True:
                    dec1 = input("Want to add another assignment? Type 'y' for yes and 'n' for no.")
                    dec1=dec1.upper()
                    if dec1 == 'Y' or dec1 == 'N':
                        dec3 = 'Y'
                        dec2 = 'Y'
                        flag = False
                        flag_add_assignment = 0
                        break
                    else:
                        print("Wrong input..")
                    
                    
            assignment_courses = []
            if dec1 == 'Y':     #Assignment info input  
                assignment_title = input("Give Assignment's title: ")            
                assignment_description = input("Give Assignment's description: ")
                print('Give date of submission using the following format : YYYY-MM-DD')
                date_format="%Y-%m-%d"
                while True:
                    try:
                        assignment_submission = input('Please give the date: ')
                        datetime.datetime.strptime(assignment_submission, date_format)   
                    except ValueError:
                        print("This is the incorrect date string format.It should be YYYY-MM-DD")
                    else:
                        print("This is the correct date format. Input successfull.")
                        break
                print("Next you need to give assignment's marks for the submitted code and for the oral mark.The number will be in %so the sum of both marks must be eqaul to 100.\n Give numbers between 0-100.")
                while True:
                    try:
                        assignment_code_mark =int(input("Give Assignment's mark for the submitted code: "))
                        assignment_oral_mark =int(input("Give Assignment's mark for the oral mark: "))
                        
                    except ValueError:
                        print('Wrong data type, please give a integer number.')
                    else:
                        if assignment_code_mark + assignment_oral_mark == 100:
                            break
                        else:
                            print('Wrong input for the marks. The sum for code mark and oral mark must be 100. E.g. code mark: 65 - oral mark: 35.Try again.')
                        
                flag2=False
                while True:
                    if flag2:
                        while True:    #decision for another language for assignment

                            dec3 = input("Want to add another language for the assignment? Type 'y' for yes and 'n' for no.")
                            dec2='Y'
                            flag = 0
                            dec3 = dec3.upper()
                            if dec3 == 'Y' or dec3 == 'N':
                                 break
                            else:
                                print("Wrong input..")
                    if dec3 == 'Y':
                        emptylist = 1
                        while  emptylist:  ##input for assignment's course language. With that i can have synchronization with the courses dict.  
                            print("Choose Assignment's language from the following language's list:\n ( Python,C#,Java,JavaScript.)")
                            while True:
                                t_l = input("Please input the assignment's Language: ")
                                t_l = t_l.lower()
                                if t_l not in languages:
                                    print('Wrong language.Please give one of the above: Python,C#,Java,JavaScript')
                                else:
                                    break
                            if t_l == 'python':
                                 course_language1='Python'
                            elif t_l == 'c#':
                                 course_language1='C#'
                            elif t_l == 'java':
                                course_language1='Java'
                            else:
                                course_language1 = 'JavaScript'
                        
                            if  courses[course_language1]:
                                emptylist = 0
                            if emptylist != 0:
                                print('List of courses for this Language is Empty. Please choose another language')
                            
                        while True:  ##input for assignments course title that depend on language.
                            if dec2 == 'Y':
                                flagg = 0
                                while not flag:
                                    print('Please choose a course title for the assignment, from the list above:')
                                    
                                    for courseTitle in courses[course_language1]:
                                       print(f'{courseTitle},',end='')
                                    assignment_courses_input=input('\nPlease input the title: ')
                                    for courseTitle in courses[course_language1]:
                                        if assignment_courses_input == courseTitle:
                                            
                                            flagg = 1
                                    if flagg==1:
                                        assignment_courses.append(assignment_courses_input)
                                        flag = 1
                                    else:
                                        print('Wrong Input.Please try again.')
                                          
                                while True:   #decision for another course title for assignment
                                    dec2 = input("Want to add another course_title for the assignment? Type 'y' for yes and 'n' for no :")
                                    dec2 = dec2.upper()
                        
                                    if dec2 == 'Y':
                                        
                                        flag = 0
                                        break
                                        
                                    elif dec2 == 'N':
                                        
                                        break
                                    else:
                                        print("Wrong input..")
                                    
                                        
                            else:
                                 break
                            flag2 = True           
                    else:
                        break
                    flag_add_assignment = True     #Above this line assignments dictionary fill with the info
                    assignments[assignment_title] = {'description':assignment_description,'dos':assignment_submission,'cm':assignment_code_mark,'om':assignment_oral_mark,'courses':assignment_courses}
            else:
                break
    return assignments    
            

def Pre_Menu1(): ##1st menu appear to user
    welcome = 'Welcome to the Private School Structure'
    plz = 'Please choose something from the menu'
    welcome = welcome.center(80)
    plz = plz.center(82)
    print('\n\n',welcome)
    print(plz)
    print('\n\n',grammes(35),end = '')
    menu1 = ' MENU'
    
    print(menu1,end='')
    print(grammes(35))
    for i in range(3):
        if i == 0:
            print(f'{i+1}. Menu for Data Input')
        elif i == 1:
            print(f'{i+1}. Menu for Data Visualization')
        else:
            print(f'{i+1}. Exit')
        
  
    print(grammes(79))
    
    while True:
        try:
            ch = int(input('Enter your choice [1-2]: '))
        except ValueError:
            print('Wrong data input.Please Enter an integer.')
            continue
        else:
            if 1 <= ch <= 3:
                break  
            else:
               print('Wrong Choise..Please enter an integer between 1-2.')
               
    
    
    return ch
    
    

def input_menu():  ##input menu
    print('\n\n',grammes(30),end = '')
    in_menu = 'DATA INPUT MENU'
    
    print(in_menu,end='')
    print(grammes(30))
    for i in range(5):  #Input menu-choices of input
        if i == 0:
            print(f'{i+1}. Courses ')
        elif i == 1:
            print(f'{i+1}. Trainers ')
        elif i == 2:
            print(f'{i+1}. Students ')
        elif i ==3  :
            print(f'{i+1}. Assignments ')
        else :
            print(f'{i+1}. Exit')
            
    print(grammes(79))
    
    while True:
        try:
            ch = int(input('Enter your choice [1-5]: '))
        except ValueError:
            print('Wrong data input..Please enter an integer.')
            continue
        else:
            if 1 <= ch <= 5:
                break
            else:
                print('Wrong Choise..Please enter an integer between 1-5.')
                
    print(grammes(79))
    return ch
 
def visualization_menu(courses,trainers,students,assignments):  ##visualization menu
    print('\n\n',grammes(28),end = '')
    in_menu = ' VISUALIZATION MENU'
    
    print(in_menu,end='')
    print(grammes(28))
    msgv = 'Please choose what you want to print.\n'
    
    print('')  
    print(msgv)
    for i in range(6):   #visualization menu - choices of print
        if i == 0:
            print(f'{i+1}. Courses list ')
        elif i == 1:
            print(f'{i+1}. Trainers list ')
        elif i == 2:
            print(f'{i+1}. Students list ')
        elif i == 3:
            print(f'{i+1}. Assignments list ')
        elif i == 4:
            print(f'{i+1}. Trainers for each language list ')
        else :
            print(f'{i+1}. Exit')
            
    print(grammes(79))
    
    while True: #choise validation
        try:
            ch_v = int(input('Enter your choice [1-5]: '))
        except ValueError:
            print('Wrong data input..Please enter an integer.')
            continue
        else:
            if 1 <= ch_v <= 6:
                break
            else:
                print('Wrong Choise..Please enter an integer between 1-5.')
                
    print(grammes(79))

    if ch_v == 1: #print of courses
        if courses:  
            print(grammes(79))
            p = 1
            print('\nThe courses of Python are: ')
            if courses['Python']: #check if exist
                for courseTitle in courses['Python']:
                    print (f"{p}. Course Title: {courseTitle}, Description: {courses['Python'][courseTitle]['description']}, Type: {courses['Python'][courseTitle]['type']}")
                    p = p+1
            else:
                print('0 courses inserted.')
            j = 1
            print('\nThe courses of Java are: ')
            if courses['Java']:
                for courseTitle in courses['Java']:
                    print (f"{j}. Course Title:{courseTitle}, Description:{courses['Java'][courseTitle]['description']}, Type:{courses['Java'][courseTitle]['type']}")
                    j = j+1
            else:
                print('0 courses inserted.')
                
            js = 1
            print('\nThe courses of JavaScript are: ')
            if courses['JavaScript']:
                for courseTitle in courses['JavaScript']:
                    print (f"{js}. Course Title:{courseTitle}, Description:{courses['JavaScript'][courseTitle]['description']}, Type:{courses['JavaScript'][courseTitle]['type']}")
                    js = js+1
            else:
                print('0 courses inserted.')
            c = 1    
            print('\nThe courses of C# are: ')
            if courses['C#']:
                for courseTitle in courses['C#']:
                    print (f"{c}. Course Title:{courseTitle}, Description:{courses['C#'][courseTitle]['description']}, Type:{courses['C#'][courseTitle]['type']}") 
                    c = c+1
            else:
                print('0 courses inserted.')
        else:
            print('Courses list is empty. Please insert first the courses.')
        print(f'\nThe sum of all courses from all languages is: {(p-1)+(j-1)+(js-1)+(c-1)}')
            
    elif ch_v == 2: #print of trainers
        if trainers:
            t = 1
            print(grammes(79))
            print('\nThe trainers are:')
            for trainer in trainers:
                print (f"{t}. First name: {trainers[trainer][ 'name']}, Last name: {trainers[trainer][ 'surname']}, Subject: {trainers[trainer][ 'specialty']}, Courses_titles: {trainers[trainer][ 'courses']}")    
                t=t+1
        else: #check for empty list
            print('Trainers list is empty. Please insert first the trainers.')
    elif ch_v ==3: #print of students
        if students:
            s=1
            print(grammes(79))
            print('\nThe students are:')
            for student in students:
                print (f"{s}. First name: {students[student][ 'name']}, Last name: {students[student][ 'surname']}, Date of birth: {students[student][ 'dob']}, Tuition Fees: {students[student][ 'tf']} ,Courses_titles: {students[student][ 'courses']}")    
                s=s+1
        else: #check for empty list
            print('Students list is empty. Please insert first the students.')
    elif ch_v==4: #print of assignments
        if assignments:
            a=1
            print('\nThe assignments are:')
            for assignment in assignments:
                print (f"{a}. Assignment Title: {assignment}, Description: {assignments[assignment]['description']}, Date of Submission: {assignments[assignment]['dos']}, Mark for the Submitted Code : {assignments[assignment]['cm']}, Mark for the Oral Mark: {assignments[assignment]['om']} , Courses_titles: {assignments[assignment]['courses']}")    
                a=a+1
        else: #check for empty list
            print('Assignments list is empty. Please insert first the assignments.')
    elif ch_v==5: #print of trainers for language given from input
        print("Trainer's availabe Languages: Python,C#,Java,JavaScript.")
        languages={'python','c#','java','javascript'}
        while True:
            c_la = input("Give the name of the Language: ")
            c_la = c_la.lower()
            if c_la not in languages:
                print('Wrong language.Please give one of the above: Python,C#,Java,JavaScript')
            else:
                break
        if c_la == 'python':
            course_la='Python'
        elif c_la == 'c#':
            course_la='C#'
        elif c_la == 'java':
            course_la='Java'
        else:
            course_la = 'JavaScript'
        languageTrainers = []
        i_i=1
        if courses[course_la]:
            print(f'\nThe trainers of {course_la} are: ')
            for courseID in courses[course_la]:
                for trainer in trainers.values():
                    if courseID in trainer['courses']:
                        if trainer not in languageTrainers:
                            languageTrainers.append(trainer)
                            print(f'{i_i}. {trainer}')
                            i_i=i_i+1
        else:
            print('There are no trainers in this language.')
    else: #exit vis menu
        print('\n')
                            
    

            
        

    
  
def main_brief():    ##main function of the module
    courses = {'Python':{},'Java':{},'C#':{},'JavaScript':{}}
    trainers = {}
    students = {}
    assignments={}
    termination_flag = 0
    while not termination_flag:
        ch = Pre_Menu1() #1st menu fucntion call and choice for the next menu
        
        if ch == 1:   #Next menu from user's choice
            input_choise = input_menu()  #call input menu
            if input_choise == 1:
                 (courses) = course_func(courses)   #Course function call - Courses inputs
                 print('\n')
                 print('Courses Input completed succesfully.')
            elif input_choise == 2:
                 if courses['Python'] or courses['Java'] or courses['C#'] or courses['JavaScript']:
                    (trainers)=Trainers_func(trainers,courses) #trainers function call - trainers inputs , if course list not empty
                 else:   
                     print("The list with the courses is empty. You can't input trainers.\n Please input  the courses first.")
            elif input_choise == 3:
                 if courses['Python'] or courses['Java'] or courses['C#'] or courses['JavaScript']:
                    (students)=Students_func(students,courses) #Student's function call - trainers inputs , if course list not empty
                 else:
                     print("The list with the courses is empty. You can't input students.\n Please input  the courses first.")
            elif input_choise == 4:
                 if courses['Python'] or courses['Java'] or courses['C#'] or courses['JavaScript']:
                    (assignments)=Assignments_func(assignments,courses) #Assignments's function call - assignments inputs , if course list not empty
                 else:
                     print("The list with the courses is empty. You can't input assignments.\n Please input  the courses first.")
            else:
                print("")
        elif ch == 2:
            if courses['Python'] or courses['Java'] or courses['C#'] or courses['JavaScript']:
                visualization_choice= visualization_menu(courses,trainers,students,assignments)    #call visualization(print) menu
            else: #print message if databese is empty and dont empty visualization menu.
                print(grammes(79))
                print('Data base is empty. Please make first inputs then try visualization menu.')
        else:
            break
     
                        
        print(grammes(79)) #baladeur help menu
        print('What would you like to do next?:\n')
        
        for i in range(2):
            if i == 0:
                print(f'{i+1}. Main Menu')
            else:
                print(f'{i+1}. Exit')
        print(grammes(79))
        while True:
            try:
                ch2 = int(input('Enter your choice [1-2]: '))
            except ValueError:
                print('Wrong data input.Please enter an integer.')
                continue
            else:
                 if 1<=ch2<=2:
                    break  
                 else:
                    print('Wrong Choise..Please enter an integer between 1-2.')
        if ch2==1:
            termination_flag=0
        else:
            break
    print(grammes(79))
    print(grammes(79)) #end of program
    print('Program terminated. Thanks for using it.\nCopyrights: Pantelakis Ioannis') 
 
     
if __name__=='main_brief()__':
    main_brief()
main_brief()
