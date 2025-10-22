import json
import random
import pathlib
from models.student import Student

currentFile = pathlib.path(__file__)

controllerDir = currentFile.parent

rootDir = controllerDir.parent

jsonFilePath = rootDir / "data" / "students.json"

def loadStudents():
    #Load students data from the JSON file.
    try:
        with open(jsonFilePath, "r", encoding='utf-8') as file:
            students_data = json.load(file)
            if not isinstance(students_data, list):
                print("Invalid data format in students file. Returning empty list.")
                return []
            return students_data
    except FileNotFoundError: 
        print("Students data file not found. Returning empty list.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON from students data file. Returning empty list.")
        return []

def saveStudents(students_data):
    #Save students data to the JSON file.
    try:
        with open(jsonFilePath, "w", encoding='utf-8') as file:
            json.dump(students_data, file, indent=4)
    except Exception as e:
        print(f"Error saving students data: {e}")

class StudentController:

    def __init__(self):
        self.students = loadStudents()\

    def _findStudentById(self, student_id: int) -> Optional[dict[str, any]]:
        #Find a student by their ID.
        for student in self.students:
            if student.get['id'] == student_id:
                return student
        return None

    def _findStudentByEmail(self, email: str) -> Optional[dict[str, any]]:
        #Find a student by their email.
        email_lower = email.lower()
        for student in self.students:
            if student.get('email') == email:
                return student
        return None

    def _generateNewStudentId(self):
        #Generate a unique student ID.
        while True:
            new_id = Student.generateStudentId()
            if self._findStudentById(new_id) is None:
                return new_id

    def registerStudent(self, name: str, email: str, password: str) -> str:
        #Register a new student.
        if not name.strip():
            return "Name cannot be empty."
        
        if not email.strip():
            return "Email cannot be empty."

        if self._findStudentByEmail(email) is not None:
            return "Email is already registered."
        
        if not password:
            return "Password cannot be empty."

        new_id = self._generateNewStudentId()

        new_student = {
            "id": new_id,
            "name": name.strip(),
            "email": email.strip(),
            "password": password,
            "subject": []
        }

        self.students.append(new_student)
        saveStudents(self.students)

        return f"Student registered successfully with ID {new_id}."

    def loginStudent(self, email: str, password: str) -> union[dict[str, any]]:
        #Login a student using email and password.
        if not email.strip():
            print("Email cannot be empty.")
            return None
        if not password:
            print("Password cannot be empty.")
            return None

        student = self._findStudentByEmail(email)

        if student:
            stored_password = student.get('password')
            if stored_password == password:
                return student
            else:
                return("Incorrect email or password.")
        else:
            return("Incorrect email or password.")


