"""
Database Model
"""

import json
from pathlib import Path
from models.student import Student

class Database:
    def __init__(self):
        # 文件路径
        self.filePath = Path(__file__).resolve().parent.parent / "data" / "student.json"

    def _ensureList(self, data):
        # 兼容 {"student":[...]} 或直接 [... ]
        if isinstance(data, dict) and "student" in data:
            return data["student"]
        if isinstance(data, list):
            return data
        return []

    """读取 JSON 文件 -> Student 对象列表"""
    def readStudents(self):
        try:
            with open(self.filePath, "r", encoding="utf-8") as f:
                raw = json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

        studentList = []
        for item in self._ensureList(raw):
            sid = str(item.get("ID") or item.get("id") or "")
            name = item.get("name", "")
            email = item.get("email", "")
            password = item.get("password", "")
            subjects = item.get("subject") or item.get("subjects") or []
            studentList.append(Student(sid, name, email, password, subjects))
        return studentList

    """写回 JSON 文件"""
    def writeStudents(self, students):
        data = []
        for s in students:
            data.append({
                "ID": s.id,
                "name": s.name,
                "email": s.email,
                "password": s.password,
                "subject": list(s.subjects or [])
            })
        with open(self.filePath, "w", encoding="utf-8") as f:
            json.dump({"student": data}, f, ensure_ascii=False, indent=4)

    def findStudentByEmail(self, email):
        email = (email or "").lower()
        for s in self.readStudents():
            if (s.email or "").lower() == email:
                return s
        return None

    def findStudentById(self, studentId):
        sid = str(studentId)
        for s in self.readStudents():
            if str(s.id) == sid:
                return s
        return None

    def addStudent(self, student):
        students = self.readStudents()
        for s in students:
            if (s.email or "").lower() == (student.email or "").lower():
                print("Student already exists.")
                return False
        students.append(student)
        self.writeStudents(students)
        return True

    def updateStudent(self, updatedStudent):
        students = self.readStudents()
        for i in range(len(students)):
            if str(students[i].id) == str(updatedStudent.id):
                students[i] = updatedStudent
                self.writeStudents(students)
                return True
        print("Student not found.")
        return False

    def removeStudent(self, studentId):
        students = self.readStudents()
        for i in range(len(students)):
            if str(students[i].id) == str(studentId):
                students.pop(i)
                self.writeStudents(students)
                return True
        print("Student not found.")
        return False

    def clearAll(self):
        with open(self.filePath, "w", encoding="utf-8") as f:
            json.dump({"student": []}, f, ensure_ascii=False, indent=4)
        return True
