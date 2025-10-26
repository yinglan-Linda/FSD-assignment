"""
Admin Controller
"""

from models.Database import Database
from collections import defaultdict

class AdminController:
    def __init__(self):
        self.db = Database()
    
    def showAllStudents(self):
        students = self.db.readStudents()
        if not students:
            return "No students in the database"        
        result = [f"{Fore.YELLOW}STUDENT LIST:{Style.RESET_ALL}"]
        for student in students:
            subjectsCount = len(student.subjects)
            result.append(f"{student.name} :: {student.id} --> EMAIL:{student.email}")
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
        if self.db.clear_all():
            print("All student data cleared by admin")
            return True, "All student data cleared successfully"
        else:
            return False, "Failed to clear database"
    
    def partitionStudents(self):
        students = self.db.readStudents()
        if not students:
            return "No students in the database"
        passStudents = [s for s in fullEnrolled if s.hasPass()]
        failStudents = [s for s in fullEnrolled if len(s.subjects) > 0 and not s.hasPassed()]
        result = [f"{Fore.YELLOW}PASS/FAIL PARTITION:{Style.RESET_ALL}"]
        result.append(f"PASS --> ")
        if passStudents:
            for student in passStudents:
                result.append(f"{student.name} :: {student.id} -->  GRADE: {getOverallGrade} - MARK:{student.calculateAverage():.2f}")
        else:
            result.append("No students in PASS category")
        result.append("")
        result.append(f"FAIL --> ")
        if failStudents:
            for student in failStudents:
                result.append(f"{student.name} :: {student.id} -->  GRADE: {getOverallGrade} - MARK:{student.calculateAverage():.2f}")
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

        gradeOrder = ["HD", "D", "C", "P", "F", "N/A"]
        result = ['{Fore.YELLOW}GRADE GROUPING:{Style.RESET_ALL}']
        
        for grade in gradeOrder:
            if grade in gradeGroups:
                studentsInGrade = gradeGroups[grade]
                result.append(f"\nGrade {grade}:")
                for student in studentsInGrade:
                    # 对于有成绩的学生，显示其平均分
                    if grade != "N/A":
                        result.append(f"{student.name} :: {student.id} -->  GRADE: {getOverallGrade} - MARK:{student.calculateAverage():.2f}")
                    else: # 对于未选课的学生
                        result.append(f"{student.name} :: {student.id} --> (No subjects enrolled)")
        return "\n".join(result)



