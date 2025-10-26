"""
Admin Controller
"""
import utils.utils as utils
import models.storage as db
from collections import defaultdict

class AdminController:
    DEFAULT_ADMIN_USERNAME = "admin"
    DEFAULT_ADMIN_PASSWORD = "Admin123"

    def __init__(self):
        self.db = db.Database()
        self.isLoggedIn = False
    
    def login(self, username, password):
        if username == self.DEFAULT_ADMIN_USERNAME and password == self.DEFAULT_ADMIN_PASSWORD:
            self.isLoggedIn = True
            return True, "Admin login successful"
        else:
            return False, "Invalid username or password"

    def logout(self):
        self.isLoggedIn = False

    def checkLogin(self):
        return self.isLoggedIn

    def showAllStudents(self):
        students = self.db.readStudents()
        if not students:
            return utils.errMSG("No students in the database")       
        result = [f"Student List:"]
        for student in students:
            # subjectsCount = len(student.subjects)
            # result.append(f"ID:{student.id}, NAME:{student.name}, EMAIL:{student.email}, SUBJECTS:{subjectsCount}")
            result.append(f"{student.name}::{student.id} --> Email:{student.email}")
        # result.append(f"Total Students: {len(students)}")
        return "\n".join(result)   
    
    def removeStudent(self, student_id):
        student = self.db.findStudentById(student_id)
        if not student:
            return False, f"Student with ID {student_id} not found"
        if self.db.removeStudent(student_id):
            return True, f"Student {student.name} (ID: {student_id}) removed successfully"
        else:
            return False, "Failed to remove student"
    
    def clearDatabase(self):
        if self.db.clearAll():
            print("All student data cleared by admin")
            return True, "All student data cleared successfully"
        else:
            return False, "Failed to clear database"
    
    def partitionStudents(self):
        students = self.db.readStudents()
        if not students:
            return utils.errMSG("No students in the database")
        fullEnrolled = [s for s in students if len(s.subjects) == 4]
        if not fullEnrolled:
            return "No students have enrolled in 4 subjects yet"
        passStudents = [s for s in fullEnrolled if s.isPass()]
        failStudents = [s for s in fullEnrolled if not s.isPass()]
        result = [f"\nPASS/FAIL PARTITION\n"]
        result.append(f"PASS ({len(passStudents)} students):")
        if passStudents:
            for student in passStudents:
                result.append(f"ID:{student.id}, NAME:{student.name}, EMAIL:{student.email}, AVGMARK:{student.get_average_mark():.2f}")
        else:
            result.append("No students in PASS category")
        result.append("")
        result.append(f"FAIL ({len(failStudents)} students):")
        if failStudents:
            result.append(f"{'ID':<10} {'Name':<20} {'Email':<30} {'Avg Mark':<10}")
            for student in failStudents:
                result.append(f"ID:{student.id}, NAME:{student.name}, EMAIL:{student.email}, AVGMARK:{student.get_average_mark():.2f}")
        else:
            result.append("No students in FAIL category")
        return "\n".join(result)
    
    def groupByGrade(self):
        students = self.db.readStudents()
        if not students:
            return "No students in the database"
        enrolledStudents = [s for s in students if s.subjects]
        if not enrolledStudents:
            return "No students have enrolled in any subjects yet"
        gradeGroups = defaultdict(list)
        for student in enrolledStudents:
            grade = student.getOverallGrade()
            gradeGroups[grade].append(student)
        gradeOrder = ["HD", "D", "C", "P", "Z", "N/A"]
        result = [f'\nGrade Grouping\n']
        for grade in gradeOrder:
            if grade in gradeGroups:
                studentsInGrade = gradeGroups[grade]
                result.append(f"Grade {grade} ({len(studentsInGrade)} students):")
                for student in studentsInGrade:
                    result.append(f"ID:{student.id}, NAME:{student.name}, EMAIL:{student.email}, AVGMARK:{student.get_average_mark():.2f}")
                result.append("")
        return "\n".join(result)

