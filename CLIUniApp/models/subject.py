import random

class Subject:
    def __init__(self, subject_id=None, mark=None):
        self.id = subject_id if subject_id else self.generateId()
        self.mark = mark if mark is not None else self.generateMark()
        self.grade = self.calculateGrade()

    @staticmethod
    def generateId():
        return f"{random.randint(1, 999):03d}"

    @staticmethod
    def generateMark():
        return random.randint(25, 100)

    def calculateGrade(self):
        if self.mark >= 85:
            return "HD"
        elif self.mark >= 75:
            return "D"
        elif self.mark >= 65:
            return "C"
        elif self.mark >= 50:
            return "P"
        else:
            return "Z"

    def __str__(self):
        return f"Subject-{self.id} -- mark = {self.mark} -- grade = {self.grade}"

    def __repr__(self):
        return f"Subject(id={self.id}, mark={self.mark}, grade={self.grade})"

