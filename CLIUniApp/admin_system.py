import utils.utils as utils
from controller.admin_controller import AdminController

""" admin system """
class AdminSystem:
    def __init__(self, controller: AdminController | None = None):
        # 创建并保存实例
        self.adminController = controller or AdminController() 

    def helpMsg(self):
        print("Admin Menu:")
        print("(c) Clear Database File")
        print("(g) Group Students by Grade")
        print("(p) Partition Students by Pass/Fail")
        print("(r) Remove a Student")
        print("(s) Show All Students")
        print("(x) Exit to Main Menu")

    """ admin main menu """
    def run(self):
        choice = utils.getInput("Admin System(c/g/p/r/s/x):")
        while (choice != 'x'):
            match choice:
                case 'c':
                    ok, msg = self.adminController.clearDatabase()
                    print(utils.infoMSG(msg) if ok else utils.errMSG(msg))
                    # AdminController.clearDatabase()
                case 'g':
                    print(self.adminController.groupByGrade())
                case 'p':
                    print(self.adminController.partitionStudents())
                case 'r':
                    sid = utils.getInput("Enter student ID to remove:")
                    ok, msg = self.adminController.removeStudent(sid)
                    print(utils.infoMSG(msg) if ok else utils.errMSG(msg))
                case 's':
                    print(self.adminController.showAllStudents())
                case 'h':
                    self.helpMsg()
                case _:
                    print(utils.infoMSG("Unavailable option. You can input 'h' to show more detail."))
            choice = utils.getInput("Start menu(c/g/p/r/s/x):") # 更新一次 user input
        utils.infoMSG("Returning to main menu...")
        return
    