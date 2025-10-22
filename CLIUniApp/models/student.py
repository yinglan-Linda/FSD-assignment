import random

class Student:
    #A class to represent a student with basic attributes and methods.
    def __init__(self, id, name, email, password, subjects_list):
        #Initialize the student with id, name, email, password, and subject list.
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects_list
    
    def _calcualteGrade(self, mark):
        #Calculate the grade based on the mark provided.
        if mark >= 85:
            return 'HD'
        elif mark >= 75:
            return 'D'
        elif mark >= 65:
            return 'C'
        elif mark >= 50:
            return 'P'
        else:
            return 'F'

    def toDictionary(self):
        #Convert the student object to a dictionary representation.
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "subject": self.subjects
        }

    def enrollSubject(self, subject_id, subject_name):
        #Enroll the student in a new subject.
        if len(self.subjects) >= 4:
            print("Cannot enroll in more than 4 subjects.")
            return False

        #Check if already enrolled in the subject
        for subject in self.subjects:
            if subject['id'] == subject_id:
                print("Already enrolled in this subject.")
                return False

        #generate random mark and calculate grade
        mark = random.randint(25, 100)
        grade = self._calcualteGrade(mark)

        #Add the new subject to the student's subject list
        new_subject_data = {
            "id": subject_id,
            "mark": mark,
            "grade": grade,
        }
        self.subjects.append(new_subject_data)
        print(f"Enrolled in subject {subject_id} successfully.")
        print(f"Assigned mark: {mark}, grade: {grade}")
        return True


    def dropSubject(self, subject_id):
        #Drop a subject from the student's enrolled subjects.
        subject_to_drop = None
        for subject in self.subjects:
            if subject['id'] == subject_id:
                subject_to_drop = subject
                break
        
        if subject_to_drop is None:
            print("Subject not found in enrolled subjects.")
            return False
        
        self.subjects.remove(subject_to_drop)
        print(f"Dropped subject {subject_id} successfully.")
        return True

    def showSubjects(self):
        #Display the list of subjects the student is enrolled in.
        if not self.subjects:
            print("No subjects enrolled.")
            return
        
        print("Enrolled Subjects:")
        for subject in self.subjects:
            print(f"Subject ID: {subject['id']}, Mark: {subject['mark']}, Grade: {subject['grade']}")
        
        avg = self.calculateAverage()
        print(f"-----------------------")
        print(f"Average Mark: {avg:.2f}")

    def calculateAverage(self):
        #Calculate the average mark across all enrolled subjects.
        if not self.subjects:
            return 0.0
        
        total_marks = 0
        for subject in self.subjects:
            total_marks += int(subject['mark'])

        average = total_marks / len(self.subjects)
        return average

    def updatePassword(self, new_password):
        #Update the student's password.
        self.password = new_password
        print("Password updated successfully.")

    def hasPassed(self):
        #Check if the student has passed all enrolled subjects.
        #A student must enroll in 4 subjects and average must be at least 50 to pass.
        if len(self.subjects) < 4:
            print("Student has not enrolled in 4 subjects, currently enrolled in", len(self.subjects))
            return False

        average = self.calculateAverage()
        if average >= 50:
            print("Student has passed with an average mark of", average)
            return True
        else:
            print("Student has not passed, average mark is", average)
            return False
        
    

        
