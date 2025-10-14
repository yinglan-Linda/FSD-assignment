import utils.utils as utils
# from colorama import Fore

""" student system """
class StudentSystem:
    def __init__(self):
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
def studentMenu(self):
    self.showMenu()

    # choice = getInput("Enter your choice: ")
    choice = utils.getInput("Student system (l/r/x):")

    while (choice != 'x'):
        match choice:
            # """ Unlogged function """
            case 'l':
                utils.infoMSG("Login successful")
                self.showMenu()
                pass 
            case 'r':
                utils.infoMSG("Register successful. You are now logged in.")
                self.showMenu()
                pass
            # """ Logged function  """
            case 'c':
                pass
            case 'e':
                pass
            case 'd':
                pass
            case 's':
                pass
            case _:
                utils.errMSG("Unavailable option.")
                # print(Fore.RED + "Unavailable option.")
        choice = utils.getInput("Enter your choice: ")  # 更新一次 user input
    
    if self.currentStudent == None:
        utils.infoMSG("Returning to main menu...")  # 返回主菜单
    else:
        self.currentStudent = None
        utils.infoMSG("Logout successful")
        utils.infoMSG("Returning to main menu...") # 返回主菜单
    return