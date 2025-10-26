"""
Database Model
"""

import json
import os
from .student import Student
from .subject import Subject

class Database:
    def __init__(self, filename='data/students.json'):
        currentDir = os.path.dirname(os.path.abspath(__file__))
        projectRoot = os.path.dirname(currentDir)
        self.filename = os.path.join(projectRoot, filename)
        self._ensureFileExists()

    def _ensureFileExists(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            self.writeStudents([])

    def readStudents(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read()
                if not content:
                    return []
                data = json.loads(content)
                
                students = []
                for studentData in data:
                    subjects = [Subject(s['id'], s['mark']) for s in studentData.get('subjects', [])]
                    students.append(Student(
                        id=studentData['id'],
                        name=studentData['name'],
                        email=studentData['email'],
                        password=studentData['password'],
                        subjectsList=subjects
                    ))
                return students
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def writeStudents(self, students):
        studentDicts = [student.toDictionary() for student in students]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(studentDicts, f, indent=4)
