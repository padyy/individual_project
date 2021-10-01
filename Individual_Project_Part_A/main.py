''' Coding Bootcamp - Individual Project Brief.
-Title:  Design of a Private School Structure
-Last name : Pantelakis
-First Name: Ioannis
-Advisors: Tyrovola Sarantia , Tzoumpa Danae, Tsipra Dafni
-Python ver:3.9.2
-win: win10 64bit
-Comments: I created dummy data for course input ,but unfortunatelly because i
 did not have more time to catch up the deadline i haven't created the dummies
 for the rest of the inputs.
'''


from u_i import User_Interface
from entities import Course_List , Student_List , Trainer_List , Assignment_List

def main():

    courses = Course_List()
    trainers = Trainer_List()
    students = Student_List()
    assignments = Assignment_List()
    ch=None
    while ch != 3:
        ch=User_Interface.Pre_Menu1() #1st menu fucntion call and choice for the next menu
        if ch == 1:   #Next menu from user's choice
            input_choise = User_Interface.Input_menu()  #call input menu
            if input_choise == 1:
                User_Interface.course_func(courses,top=True)   #Course function call - Courses inputs
            elif input_choise == 2:
                User_Interface.Trainers_func(trainers,courses,top=True) #trainers function call - trainers inputs , if course list not empty    
            elif input_choise == 3:
                User_Interface.Students_func(students,courses,top=True)
            elif input_choise == 4:
                User_Interface.Assignments_func(assignments,courses,top=True) #Assignments's function call - assignments inputs , if course list not empty
            else:
                print("")
        elif ch == 2:
            User_Interface.visualization_menu(courses,trainers,students,assignments)    #call visualization(print) menu    
    User_Interface.exitprogram()
if __name__=='__main()__':
    main()

main()   
