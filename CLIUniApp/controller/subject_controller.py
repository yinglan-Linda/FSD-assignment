from models.subject import Subject
import utils.utils as utils
import models.database as db
import logging
import re

_THREE_DIGIT_ID = re.compile(r"^(?:0[0-9]{2}|[1-9][0-9]{2})$")

class SubjectController:
    def __init__(self, student_controller):
        self.student_controller = student_controller

    def enrol_subject(self):
        student = self.student_controller.get_current_student()
        if not student:
            return False, "Please login first"
        if not student.can_enrol():
            return False, "Students are allowed to enrol in 4 subjects only"

        existingIds = {s.id for s in getattr(student, "subjects", [])}
        subject = Subject()
        while subject.id in existingIds:
            subject = Subject()

        success, msg = student.enrol_subject(subject)
        if success:
            if self.student_controller.update_current_student():
                logging.info(f"Student {student.id} enrolled in subject {subject.id}")
            else:
                logging.warning(f"Persist failed after enrol: student {student.id}, subject {subject.id}")
        else:
            logging.debug(f"Enrol failed for student {getattr(student, 'id', '?')}: {msg}")
        return success, msg

    def remove_subject(self, subject_id):
        student = self.student_controller.get_current_student()
        if not student:
            return False, "Please login first"
        if not isinstance(subject_id, str) or not _THREE_DIGIT_ID.match(subject_id):
            return False, "Invalid subject ID. Please enter a 3-digit ID (001–999)."

        success, msg = student.remove_subject(subject_id)
        if success:
            if self.student_controller.update_current_student():
                logging.info(f"Student {student.id} removed subject {subject_id}")
            else:
                logging.warning(f"Persist failed after remove: student {student.id}, subject {subject_id}")
        else:
            logging.debug(f"Remove failed {subject_id} for student {getattr(student, 'id', '?')}: {msg}")
        return success, msg

    def show_subjects(self):
        student = self.student_controller.get_current_student()
        if not student:
            return "Please login first"
        if hasattr(student, "detailed_info") and callable(student.detailed_info):
            return student.detailed_info()

        subjects = getattr(student, "subjects", [])
        if not subjects:
            return "No subjects enrolled yet."
        lines = [str(s) for s in subjects]
        avg = getattr(student, "average_mark", None)
        if avg is not None:
            lines.append(f"Average mark = {avg:.2f}")
        return "\n".join(lines)

    def change_password(self, new_password):
        
        student = self.student_controller.get_current_student()
        if not student:
            return False, "Please login first"

        valid, msg = utils.validatePassword(new_password)
        if not valid:
            return False, msg

        student.change_password(new_password)
        if self.student_controller.update_current_student():
            logging.info(f"Student {student.id} changed password")
            return True, "Password changed successfully"
        logging.error(f"Failed to persist password change for student {student.id}")
        return False, "Failed to update password"
