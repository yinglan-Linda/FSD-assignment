import utils.utils as utils
from controller.student_controller import StudentController
from controller.subject_controller import SubjectController
import getpass

""" student system """
class StudentSystem:
    def __init__(self, controller: StudentController): 
        self.studentController = StudentController()
        self.subjectController = SubjectController(self.studentController)   # 创建实例
        self.currentStudent = None        # None 表示未登录/未注册

    def showMenu(self):
        if self.currentStudent == None:   # 未登录菜单
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

            if self.currentStudent == None:
                
                choice = utils.getInput("Student system (l/r/x):")
                
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
                
                choice = utils.getInput("Student Course Menu (c/e/d/s/x):")
                
                match choice:
                    # """ Logged function  """
                    case 'c':
                        self.subjectController.change_password()
                    case 'e':
                        self.subjectController.enrol_subject()
                    case 'd':
                        self.subjectController.remove_subject()
                    case 's':
                        print(self.subjectController.show_subjects())
                    case 'x':
                        self._handleLogout()
                        print(utils.infoMSG("Logout successful"))
                        print(utils.infoMSG("Returning to main menu..."))
                        break
                    case _:
                        print(utils.errMSG("Unavailable option."))

    def _handleLogin(self):
        #login handler
        print("Student Login selected") 
        email = utils.getInput("Enter email: ")
        password = getpass.getpass("Enter password: ")

        if not utils.validateEmail(email):
            utils.errMSG("Invalid email format.")
            return
    
        result = self.studentController.loginStudent(email, password)

        if isinstance(result, dict):
            self.currentStudent = result
            utils.infoMSG("Login successful")
        else:
            utils.errMSG(result)

    def _handleRegister(self):
        #register handler
        print("Student Register selected")
        name = utils.getInput("Enter name: ")
        email = utils.getInput("Enter email: ")
        

        if not utils.validateEmail(email):
            utils.errMSG("Invalid email format.")
            utils.errMSG("Email must ended with '@university.com'.")
            return
    
        if self.studentController.check_email_exists(email):
            utils.errMSG("Email is already registered.")
            return
            
        utils.infoMSG("Email Available.")
        password = getpass.getpass("Enter password: ")
        
        if not utils.validatePassword(password):
            utils.errMSG("Invalid password format.")
            return

        message = self.studentController.registerStudent(name, email, password)

        if "successfully" in message:
            self.currentStudent = self.studentController._findStudentByEmail(email)
            utils.infoMSG("Register successful. You are now logged in.")

    def _handleLogout(self):
        #logout handler
        if self.currentStudent:
            utils.infoMSG("Logging out...")
            self.currentStudent = None