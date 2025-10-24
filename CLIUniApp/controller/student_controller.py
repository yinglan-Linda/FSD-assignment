import json
import random
import pathlib
from models.student import Student

currentFile = pathlib.Path(__file__)

controllerDir = currentFile.parent

rootDir = controllerDir.parent

jsonFilePath = rootDir / "data" / "student.json"

def loadStudents() -> list[dict[str, any]]:
    #Load students data from the JSON file.
    try:
        with open(jsonFilePath, "r", encoding='utf-8') as file:
            data = json.load(file)
            
            if isinstance(data, dict) and 'student' in data:
                student_list = data['student']
                if isinstance(student_list, list):
                    return student_list
                
            if isinstance(data, list):
                return data
            # if not isinstance(students_data, list):
            #     print("Invalid data format in students file. Returning empty list.")
            #     return []
            # return students_data
    except FileNotFoundError: 
        print("Students data file not found. Returning empty list.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON from students data file. Returning empty list.")
        return []

def saveStudents(data: list[dict[str, any]]) -> None:
    #Save students data to the JSON file.
    try:
        data_to_save = {"student": data}
        with open(jsonFilePath, "w", encoding='utf-8') as file:
            json.dump(data_to_save, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving students data: {e}")

class StudentController:

    def __init__(self):
        self.students = loadStudents()\

    def _findStudentById(self, student_id: int) -> dict[str, any]:
        #Find a student by their ID.
        for student in self.students:
            id_value = student.get('id')
            
            if id_value is None:
                id_value = student.get('ID')
            
            if id_value is not None:
                if str(id_value) == str(student_id):
                    return student
        return None

    def _findStudentByEmail(self, email: str) -> dict[str, any]:
        #Find a student by their email.
        email_lower = email.lower()
        for student in self.students:
            if student.get('email', '').lower() == email_lower:
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
            "ID": new_id,
            "name": name.strip(),
            "email": email.strip(),
            "password": password,
            "subject": []
        }

        self.students.append(new_student)
        saveStudents(self.students)

        return f"Student registered successfully with ID {new_id}."

    def loginStudent(self, email: str, password: str) -> dict[str, any]:
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
        
        # if student:
        #     # --- (1. ADD THESE DEBUG LINES) ---
        #     stored_password = student.get("password")
        #     print("\n[DEBUG] --- Verifying Login ---")
        #     print(f"[DEBUG] Email found for user: {student.get('name')}")
        #     print(f"[DEBUG] Password from JSON: '{stored_password}' (Type: {type(stored_password)})")
        #     print(f"[DEBUG] Password you typed: '{password}' (Type: {type(password)})")
        #     print("[DEBUG] -------------------------\n")
        #     # --- (END OF DEBUG LINES) ---

        #     if stored_password == password: # The actual comparison
        #         return student  # 登录成功！
        #     else:
        #         return "错误：Email 或密码不正确。"
        # else:
        #     # --- (2. ADD THIS DEBUG LINE) ---
        #     print(f"\n[DEBUG] No student found with email: '{email}'\n")
        #     # --- (END OF DEBUG LINE) ---
        #     return "错误：Email 或密码不正确。"


