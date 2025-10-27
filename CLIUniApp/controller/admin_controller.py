"""
Admin Controller
"""
import utils.utils as utils
import models.storage as db
from collections import defaultdict

class AdminController:
    def __init__(self):
        self.db = db.Database()
        
    def showAllStudents(self):
        students = self.db.readStudents()
        # students = None
        if not students:
            return utils.errMSG("No students in the database")       
        result = [utils.infoMSG("Student List:")]
        # result.append(utils.infoMSG("Student List:"))
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
    
    def _confirm_action(self, action_message: str) -> bool:
        """
        Asks for a generic confirmation from the user.
        Returns True if the user confirms with 'yes'.
        """
        # e.g., action_message = "delete ALL student data"
        print(utils.errMSG(f"This will {action_message}! This action cannot be undone."))
        confirmation = utils.getInput("Are you sure? (y/n): ")
        return confirmation == "y"
    
    def clearDatabase(self):
        if self._confirm_action("clear the entire student database"):
            self.db.clearAll()
            return True, "All student data cleared successfully"
        else:
            return False, "Failed to clear database"
            # print(utils.infoMSG("Clear database action cancelled."))
        # if self.db.clearAll():
        #     print("All student data cleared by admin")
        #     return True, "All student data cleared successfully"
        # else:
        #     return False, "Failed to clear database"
    
    def partitionStudents(self):
        students = self.db.readStudents()
        if not students:
            return "No students in the database"
        passStudents = [s for s in students if s.hasPassed()]
        failStudents = [s for s in students if len(s.subject) > 0 and not s.hasPassed()]
        result = [utils.infoMSG("PASS/FAIL PARTITION:")]
        result.append(f"PASS --> ")
        if passStudents:
            for student in passStudents:
                result.append(f"{student.name} :: {student.id} -->  GRADE: {student.getOverallGrade()} - MARK:{student.calculateAverage():.2f}")
        else:
            result.append("No students in PASS category")
        result.append(f"FAIL --> ")
        if failStudents:
            for student in failStudents:
                result.append(f"{student.name} :: {student.id} -->  GRADE: {student.getOverallGrade()} - MARK:{student.calculateAverage():.2f}")
        else:
            result.append("No students in FAIL category")
        return "\n".join(result)
    
    def groupByGrade(self):
        students = self.db.readStudents()
        if not students:
            return "No students in the database."
        gradeGroups = defaultdict(list)
        for student in students:
            overallGrade = student.getOverallGrade()
            gradeGroups[overallGrade].append(student)
        if not gradeGroups:
            return "No student data available for grouping."

        gradeOrder = ["HD", "D", "C", "P", "Z", "N/A"]
        result = [utils.infoMSG("GRADE GROUPING:")]
        
        for grade in gradeOrder:
            if grade in gradeGroups:
                studentsInGrade = gradeGroups[grade]
                result.append(f"Grade {grade}:")
                for student in studentsInGrade:
                    # 对于有成绩的学生，显示其平均分
                    if grade != "N/A":
                        result.append(f"{student.name} :: {student.id} -->  GRADE: {student.getOverallGrade()} - MARK:{student.calculateAverage():.2f}")
                    else: # 对于未选课的学生
                        result.append(f"{student.name} :: {student.id} --> (No subjects enrolled)")
        return "\n".join(result)

