from utils.utils import getInput, infoMSG, errMSG, validate_email, validate_password
import utils.utils as utils
from controller.student_controller import StudentController

""" student system """
class StudentSystem:
    def __init__(self):
        self.studentController = StudentController()
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

        choice = utils.getInput("Student system (l/r/x):")

        if self.currentStudent == None:
            match choice:
                # """ Unlogged function """
                case 'l':
                    self._handleLogin()
                case 'r':
                    self._handleRegister()
                case 'x':
                    utils.infoMSG("Returning to main menu...")
                    break
                case _:
                    utils.errMSG("Unavailable option.")
        else:
            match choice:
                # """ Logged function  """
                case 'c':
                    pass
                case 'e':
                    pass
                case 'd':
                    pass
                case 's':
                    pass
                case 'x':
                    self._handleLogout()
                    utils.infoMSG("Logout successful")
                    utils.infoMSG("Returning to main menu...")
                    break
                case _:
                    utils.errMSG("Unavailable option.")

def _handleLogin(self):
    #login handler
    print("Student Login selected") 
    email = utils.getInput("Enter email: ")
    password = utils.getInput("Enter password: ")

    if not utils.validate_email(email):
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
    password = utils.getInput("Enter password: ")

    if not utils.validate_email(email):
        utils.errMSG("Invalid email format.")
        return
    
    if not utils.validate_password(password):
        utils.errMSG("Invalid password format.")
        return
    
    message = self.studentController.registerStudent(name, email, password)

    if "successfully" in message:
        self.currentStudent = self.studentController._findStudentByEmail(email)
        utils.infoMSG("Register successful. You are now logged in.")

def _handleLogout(self):
    #logout handler
    if self.currentStudent:
        infoMSG("Logging out...")
        self.currentStudent = None





    # self.showMenu()

    # # choice = getInput("Enter your choice: ")
    # choice = utils.getInput("Student system (l/r/x):")

    # while (choice != 'x'):
    #     match choice:
    #         # """ Unlogged function """
    #         case 'l':
    #             utils.infoMSG("Login successful")
    #             self.showMenu()
    #             pass 
    #         case 'r':
    #             utils.infoMSG("Register successful. You are now logged in.")
    #             self.showMenu()
    #             pass
    #         # """ Logged function  """
    #         case 'c':
    #             pass
    #         case 'e':
    #             pass
    #         case 'd':
    #             pass
    #         case 's':
    #             pass
    #         case _:
    #             utils.errMSG("Unavailable option.")
    #             # print(Fore.RED + "Unavailable option.")
    #     choice = utils.getInput("Enter your choice: ")  # 更新一次 user input
    
    # if self.currentStudent == None:
    #     utils.infoMSG("Returning to main menu...")  # 返回主菜单
    # else:
    #     self.currentStudent = None
    #     utils.infoMSG("Logout successful")
    #     utils.infoMSG("Returning to main menu...") # 返回主菜单
    # return