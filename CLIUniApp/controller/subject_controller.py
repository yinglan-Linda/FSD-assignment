from models.subject import Subject
import utils.utils as utils
import logging
import re

_THREE_DIGIT_ID = re.compile(r"^(?:0[0-9]{2}|[1-9][0-9]{2})$")

class SubjectController:
    # Handles subject actions for the current student
    def __init__(self, studentController):
        self.studentController = studentController

    def enrol_subject(self):
        student = self.studentController.getCurrentStudent()
        if not student:
            return False, "Please login first"
        # if not student.enrol():
        #     return False, "Students are allowed to enrol in 4 subjects only"

        existingIds = {s.id for s in student.subject}
        newSubject = Subject()
        while newSubject.id in existingIds:
            newSubject = Subject()

        # 4-subject limit is enforced inside student.enrol(...)
        success, msg = student.enrol(newSubject)
        if success:
            if self.studentController.updateCurrentStudent():
                logging.info(f"Student {student.id} enrolled in subject {newSubject.id}")
            else:
                logging.warning(f"Persist failed after enrol: student {student.id}, subject {newSubject.id}")
        else:
            logging.debug(f"Enrol failed for student {getattr(student, 'id', '?')}: {msg}")
        return success, msg

    def remove_subject(self, subject_id):
        # validate id, remove subject, then save
        student = self.studentController.getCurrentStudent()
        if not student:
            return False, "Please login first"
        if not isinstance(subject_id, str) or not _THREE_DIGIT_ID.match(subject_id):
            return False, "Invalid subject ID. Please enter a 3-digit ID (001–999)."

        success, msg = student.drop(subject_id)
        if success:
            if self.studentController.updateCurrentStudent():
                logging.info(f"Student {student.id} removed subject {subject_id}")
            else:
                logging.warning(f"Persist failed after remove: student {student.id}, subject {subject_id}")
        else:
            logging.debug(f"Remove failed {subject_id} for student {getattr(student, 'id', '?')}: {msg}")
        return success, msg

    def show_subjects(self) ->str:
        # return the student's formatted subject list and average
        student = self.studentController.getCurrentStudent()
        if not student:
            return "Please login first"
        
        return student.detailedInfo()

    def change_password(self, new_password):
        # validate, update password, then save
        student = self.studentController.getCurrentStudent()
        if not student:
            return False, "Please login first"

        valid = utils.validatePassword(new_password)
        if not valid:
            return False, "Invalid password format"

        student.password = new_password
        
        if self.studentController.updateCurrentStudent():
            return True, "Password changed successfully"

