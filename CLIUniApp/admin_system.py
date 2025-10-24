import utils.utils as utils

""" admin system """
class AdminSystem:    
    def helpMsg(self):
        print("Admin Menu:")
        print("(c) Clear Database File")
        print("(g) Group Students by Grade")
        print("(p) Partition Students by Pass/Fail")
        print("(r) Remove a Student")
        print("(s) Show All Students")
        print("(x) Exit to Main Menu")
        # utils.getInput("Start menu(c/g/p/r/s/x):")

""" admin main menu """
def adminMenu(self):
    choice = utils.getInput("Start menu(c/g/p/r/s/x):")
    while (choice != 'x'):
        match choice:
            case 'c':
                pass
            case 'g':
                pass
            case 'p':
                pass
            case 'r':
                pass
            case 's':
                pass
            case 'h':
                self.helpMsg()
            case _:
                # print("Unavailable option. You can input 'h' to show more detail.")
                utils.infoMSG("Unavailable option. You can input 'h' to show more detail.")
        choice = utils.getInput("Start menu(c/g/p/r/s/x):") # 更新一次 user input
    utils.infoMSG("Returning to main menu...")
    return
    