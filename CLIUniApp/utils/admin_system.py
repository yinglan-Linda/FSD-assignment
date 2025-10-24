    def getStudentId(self):
        studentId = input("Enter student ID to remove: ").strip()
        return studentId
    
    def confirmClearDatabase(self):
        print("\nThis will delete ALL student data!")
        confirmation = input("Are you sure? (yes/no): ").strip().lower()
        return confirmation == "yes"
    
    def confirmRemoveStudent(self, studentId):
        confirmation = input(f"Are you sure you want to remove student {studentId}? (yes/no): ").strip().lower()
        return confirmation == "yes"
    
    def showStudents(self, info):
        print(info)
    
    def showPartition(self, info):
        print(info)
    
    def showGrouping(self, info):
        print(info)
    
