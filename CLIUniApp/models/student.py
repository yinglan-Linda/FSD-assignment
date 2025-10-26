import random
from models.subject import Subject
from typing import List, Tuple, Optional, Dict, Any

class Student:
    #A class to represent a student with basic attributes and methods.
    def __init__(self, name: str, email: str, password: str, subject: Optional[list[Dict[str, Any]]], ID: Optional[str] = None, **kwargs):
        #create a student object from json data
        self.id = ID if ID else kwargs.get('id')
        self.name: str = name
        self.email: str = email
        self.password: str = password
        
        if self.id is None:
            self.id = self.generateStudentId()
            
        
        self.subject: List[Subject] = []
        subject = subject or kwargs.get("subject") or []
        
        for subjectData in subject:
            self.subject.append(
                Subject(
                    subject_id = subjectData.get("id"),
                    mark = subjectData.get("mark")
                )
            )
    
    def toDictionary(self) -> dict:
        #Convert the student object to a dictionary representation.
        return {
            "ID": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "subject": [subject.toDict() for subject in self.subject]
        }
        
    def enrol(self, subjecttoEnroll: Subject) -> Tuple[bool, str]:
        #Enrol subjects
        if len(self.subject) >= 4:
            return False, f"Student are allowed to enrol in 4 subjects only"
        
        existingIds = {s.id for s in self.subject}
        if subjecttoEnroll.id in existingIds:
            return False, f"Already enrolled in subject {subjecttoEnroll.id}"
        
        self.subject.append(subjecttoEnroll)
        return True, f"Enrolled in subject {subjecttoEnroll.id} successfully."

    def drop(self, subject_id: str) -> bool:
        #Drop a subject from the student's enrolled subjects.
        subjecttoDrop = None
        for subject in self.subject:
            if subject.id == subject_id:
                subjecttoDrop = subject
                break
        
        if subjecttoDrop:
            self.subject.remove(subjecttoDrop)
            return True, f"Dropped subject {subject_id} successfully."
        else:
            return False, f"Subject {subject_id} not found in enrolled subjects."
    

    def listSubjects(self) -> list[Subject]:
        #Display the list of subjects the student is enrolled in.
        return list(self.subject)

    def calculateAverage(self):
        #Calculate the average mark across all enrolled subjects.
        if not self.subject:
            return 0.0
        
        total_marks = 0
        for subject in self.subject:
            total_marks += int(subject.mark)

        average = total_marks / len(self.subject)
        return average

    def changePassword(self, new_password):
        #Update the student's password.
        self.password = new_password
        print("Password updated successfully.")

    def hasPassed(self):
        #Check if the student has passed all enrolled subjects.
        #A student must enroll in 4 subjects and average must be at least 50 to pass.
        if len(self.subject) < 4:
            #print("Student has not enrolled in 4 subjects, currently enrolled in", len(self.subject))
            return False

        average = self.calculateAverage()
        if average >= 50:
            #print("Student has passed with an average mark of", average)
            return True
        else:
            #print("Student has not passed, average mark is", average)
            return False
        
        
    def detailedInfo(self) -> str:
        #detailed subject info
        if not self.subject:
            return f"No subjects enrolled yet."
        
        lines = [str(subject) for subject in self.subject]
        avg = self.calculateAverage()
        lines.append("-----------------------")
        lines.append(f"Average Mark: {avg: .2f}")
        
        if len(self.subject) >= 4:
            if self.hasPassed():
                lines.append("Status: PASS ✅")
            else:
                lines.append("Status: FAIL ❌ (average < 50 or <4 subjects)")
        else:
            lines.append("Status: In Progress (need 4 subjects)")
        
        lines.append("")
        return "\n".join(lines)
    
    @staticmethod
    def _generateStudentId():
        #Generate a random student ID between 100000 and 999999.
        return str(random.randint(100000, 999999))
    
    def getOverallGrade(self):
        if not self.subjects:
            return "N/A"

        avg = self.calculateAverage()
        if avg >= 85: return "HD"
        if avg >= 75: return "D"
        if avg >= 65: return "C"
        if avg >= 50: return "P"
        return "F"
        
