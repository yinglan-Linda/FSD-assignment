"""
Database Model
"""

import pickle
import os

class Database:
    def __init__(self, filename='students.data'):

        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        self.filename = os.path.join(parent_dir, filename)
        
        self.initialize()
    
    def initialize(self):

        try:
            if not os.path.exists(self.filename):
                with open(self.filename, 'wb') as f:
                    pickle.dump([], f)
                print(f"[INFO] Created new database file: {self.filename}")
            else:
                print(f"[INFO] Database file exists: {self.filename}")
        except Exception as e:
            print(f"[ERROR] Error initializing database: {e}")
    
    def readStudents(self):

        try:
            with open(self.filename, 'rb') as f:
                students = pickle.load(f)
            print(f"[INFO] Read {len(students)} students from database")
            return students
        except FileNotFoundError:
            print("[WARNING] Database file not found, returning empty list")
            return []
        except EOFError:
            print("[WARNING] Database file is empty, returning empty list")
            return []
        except Exception as e:
            print(f"[ERROR] Error reading database: {e}")
            return []
    
    def writeStudents(self, students):

        try:
            with open(self.filename, 'wb') as f:
                pickle.dump(students, f)
            print(f"[INFO] Wrote {len(students)} students to database")
            return True
        except Exception as e:
            print(f"[ERROR] Error writing to database: {e}")
            return False
    
    def addStudent(self, student):

        students = self.readStudents()
        
        if any(s.email == student.email for s in students):
            print(f"[WARNING] Student with email {student.email} already exists")
            return False
        
        students.append(student)
        return self.writeStudents(students)
    
    def findStudentByEmail(self, email):

        students = self.readStudents()
        for student in students:
            if student.email == email:
                return student
        return None
    
    def findStudentById(self, student_id):

        students = self.readStudents()
        for student in students:
            if student.id == student_id:
                return student
        return None
    
    def updateStudent(self, updated_student):

        students = self.readStudents()
        
        for i, student in enumerate(students):
            if student.id == updated_student.id:
                students[i] = updated_student
                return self.writeStudents(students)
        
        print(f"[WARNING] Student with ID {updated_student.id} not found")
        return False
    
    def removeStudent(self, student_id):

        students = self.readStudents()
        
        for i, student in enumerate(students):
            if student.id == student_id:
                removed = students.pop(i)
                print(f"[INFO] Removed student: {removed.name} (ID: {student_id})")
                return self.writeStudents(students)
        
        print(f"[WARNING] Student with ID {student_id} not found")
        return False
    
    def clearAll(self):

        try:
            with open(self.filename, 'wb') as f:
                pickle.dump([], f)
            print("[INFO] Cleared all student data")
            return True
        except Exception as e:
            print(f"[ERROR] Error clearing database: {e}")
            return False
    
    def checkStudentExists(self, email):

        return self.findStudentByEmail(email) is not None