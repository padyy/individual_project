
import mysql.connector
import datetime

class Db_handler: #class for db functions

#config = {'host' : 'localhost', 'user' : 'root', 'password' : 'PadyPp2441990' }
    
    def __init__(self,host,user,password,dbName):
        self.config = {'host' : host, 'user' : user, 'password' : password }
        self.dbName = dbName

    def connect(self): #connection with db
        self.conn = mysql.connector.connect(**self.config)

    def commit(self): #commit changes
        self.conn.commit()

    def getCursor(self): #initialization of cursor 
        PadyCursor = self.conn.cursor()
        PadyCursor.execute('USE '+self.dbName)
        return PadyCursor

    def disconnect(self): #close connections
        self.conn.cursor().close()
        self.conn.close()
        
    def createDB(self): #create db only if not exist
        PadyCursor = self.conn.cursor()

        try:
            PadyCursor.execute('USE '+self.dbName)
        except:
            try:
                PadyCursor.execute('CREATE DATABASE '+self.dbName)
            except Exception as ex:
                print(ex)
            PadyCursor.execute('USE '+self.dbName)
            try:
                PadyCursor.execute('CREATE TABLE students(st_id int NOT NULL AUTO_INCREMENT, '\
                               'first_name varchar(16) NOT NULL, '\
                               'last_name varchar(16) NOT NULL, '\
                               'birthdate date NOT NULL, '\
                               'student_fees int NOT NULL, '\
                               'PRIMARY KEY(st_id), '\
                               'CONSTRAINT UC_Student UNIQUE (first_name,last_name));')      
            except Exception as ex:
                print(ex)


            try:
                PadyCursor.execute('CREATE TABLE trainers(tr_id int NOT NULL AUTO_INCREMENT, '\
                               'first_name varchar(16) NOT NULL, '\
                               'last_name varchar(16) NOT NULL, '\
                               'trainer_subject varchar(16) NOT NULL, '\
                               'PRIMARY KEY(tr_id), '\
                               'CONSTRAINT UC_Trainer UNIQUE (first_name,last_name));')
            except Exception as ex:
                print(ex)
               
            try:
                PadyCursor.execute('CREATE TABLE assignments(as_id int NOT NULL AUTO_INCREMENT, '\
                               'as_title varchar(128) UNIQUE NOT NULL, '\
                               'as_descritpion varchar(256) NOT NULL, '\
                               'as_submission date NOT NULL, '\
                               'acm double NOT NULL, '\
                               'aom double NOT NULL, '\
                               'PRIMARY KEY(as_id));')
            except Exception as ex:
                print(ex)

            try:
                PadyCursor.execute('CREATE TABLE courses(c_id int NOT NULL AUTO_INCREMENT, '\
                               'language varchar(12) NOT NULL, '\
                               'course_type varchar(12) NOT NULL, '\
                               'title varchar(12) UNIQUE NOT NULL, '\
                               'description varchar(256) NOT NULL, '\
                               'PRIMARY KEY(c_id));')
            except Exception as ex:
                print(ex)





            try:
                PadyCursor.execute('CREATE TABLE student_courses('\
                               'st_id int NOT NULL, '\
                               'c_id int NOT NULL, '\
                               'PRIMARY KEY(st_id,c_id), '\
                               'FOREIGN KEY (st_id) REFERENCES students(st_id), '\
                               'FOREIGN KEY (c_id) REFERENCES courses(c_id));')    
            except Exception as ex:
                print(ex)

            try:
                PadyCursor.execute('CREATE TABLE trainer_courses('\
                               'tr_id int NOT NULL, '\
                               'c_id int NOT NULL, '\
                               'PRIMARY KEY(tr_id,c_id), '\
                               'FOREIGN KEY (tr_id) REFERENCES trainers(tr_id), '\
                               'FOREIGN KEY (c_id) REFERENCES courses(c_id));')
            except Exception as ex:
                print(ex)

            try:
                PadyCursor.execute('CREATE TABLE course_assignments('\
                               'as_id int NOT NULL, '\
                               'c_id int NOT NULL, '\
                               'PRIMARY KEY(as_id,c_id), '\
                               'FOREIGN KEY (as_id) REFERENCES assignments(as_id), '\
                               'FOREIGN KEY (c_id) REFERENCES courses(c_id));')
            except Exception as ex:
                print(ex)

      
