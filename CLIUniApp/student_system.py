import utils.utils as utils
from controller.student_controller import StudentController
from controller.subject_controller import SubjectController
import getpass

""" student system """
class StudentSystem:
    def __init__(self, controller: StudentController): 
        self.studentController = controller
        self.subjectController = SubjectController(self.studentController)
        self.currentStudent = None        # None 表示未登录/未注册

    def _isLoggedIn(self):
        return self.studentController.getCurrentStudent() is not None
    
    def _getLoggedInStudent(self):
        return self.studentController.getCurrentStudent()

    def showMenu(self):
        if not self._isLoggedIn():   # 未登录菜单
            print("(l) Login")
            print("(r) Register")
            print("(x) Exit to Main Menu")
        else:
            print("Student Course Menu") # 已登录菜单
            print("(c) Change Password")
            print("(e) Enrol in Subject")
            print("(d) Delete Enrolled Subject")
            print("(s) Show Enrolled Subjects")
            print("(x) Exit to Main Menu") 

    """ student main menu """
    def run(self):
        while True:
            self.showMenu()

            if not self._isLoggedIn():
                
                choice = utils.getInput("Student system (l/r/x):").strip().lower()
                
                match choice:
                    # """ Unlogged function """
                    case 'l':
                        self._handleLogin()
                    case 'r':
                        self._handleRegister()
                    case 'x':
                        print(utils.infoMSG("Returning to main menu..."))
                        break
                    case _:
                        print(utils.errMSG("Unavailable option."))
            else:
                
                choice = utils.getInput("Student Course Menu (c/e/d/s/x):").strip().lower()
                
                match choice:
                    # """ Logged function  """
                    case 'c':
                        self._handleChangePassword()
                    case 'e':
                        self._handleEnrolSubject()
                    case 'd':
                        self._handleRemoveSubject()
                    case 's':
                        details = self.subjectController.show_subjects()
                        print(details)
                    case 'x':
                        self._handleLogout()
                        print(utils.infoMSG("Logout successful"))
                        print(utils.infoMSG("Returning to main menu..."))
                        break
                    case _:
                        print(utils.errMSG("Unavailable option."))

    def _handleLogin(self):
        #login handler
        print(utils.greenMSG("Student Login selected"))
        email = utils.getInput("Enter email: ").strip()
        #password = getpass.getpass("Enter password: ")
        #show password for testing purpose
        password = input("Enter password: ").strip()

        if not utils.validateEmail(email):
            print(utils.errMSG("Invalid email format."))
            return
    
        studentObj = self.studentController.loginStudent(email, password)

        if studentObj is None:
            print(utils.errMSG("Login failed. Check email/password."))
            return
        
        print(utils.infoMSG(f"Login successful. Welcome, {studentObj.name}!"))

    def _handleRegister(self):
        #register handler
        print(utils.greenMSG("Student Register selected"))
        name = utils.getInput("Enter name: ").strip()
        email = utils.getInput("Enter email: ").strip()
        

        if not utils.validateEmail(email):
            print(utils.errMSG("Invalid email format."))
            print(utils.errMSG("Email must ended with '@university.com'."))
            return
    
        if self.studentController.checkEmailExists(email):
            print(utils.errMSG("Email is already registered."))
            return
            
        print(utils.infoMSG("Email Available."))
        #password = getpass.getpass("Enter password: ")
        #show password for testing purpose
        password = input("Enter password: ").strip()
        
        if not utils.validatePassword(password):
            print(utils.errMSG("Invalid password format."))
            return


        message = self.studentController.registerStudent(name, email, password)
        print(utils.infoMSG(message))

        if "successfully" in message:
            self.currentStudent = self.studentController._findStudentByEmail(email)
            print(utils.infoMSG("Register successful. Please Login."))

    def _handleLogout(self):
        #logout handler
        if self.currentStudent:
            print(utils.infoMSG("Logging out..."))
            self.studentController.currentStudent = None
            
    def _handleChangePassword(self):
        #handle password change
        if not self._isLoggedIn():
            print(utils.errMSG("Please Login First."))
            return
        
        newPassword = input("Enter new Password: ").strip()
        
        ok, msg = self.subjectController.change_password(newPassword)
        if ok:
            print(utils.infoMSG(msg))
        else:
            print(utils.errMSG(msg))
            
    def _handleEnrolSubject(self):
        #handle enrollment
        if not self._isLoggedIn():
            print(utils.errMSG("Please Login First."))
            return
        
        ok, msg = self.subjectController.enrol_subject()
        if ok:
            print(utils.infoMSG(msg))
        else:
            print(utils.errMSG(msg))
            
    def _handleRemoveSubject(self):
        #handle drop subjects
        if not self._isLoggedIn():
            print(utils.errMSG("Please Login First."))
            return
        
        subjectId = utils.getInput("Enter subject ID to delete: ").strip()
        
        ok, msg = self.subjectController.remove_subject(subjectId)
        if ok:
            print(utils.infoMSG(msg))
        else:
            print(utils.errMSG(msg))
            
    def _handleShowSubjects(self):
        #handle display subjects
        if not self._isLoggedIn():
            print(utils.errMSG("Please Login First."))
            return
        
        details = self.subjectController.show_subjects()
        print(details)