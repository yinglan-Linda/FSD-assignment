from utils.utils import getInput

""" admin system """
class AdminSystem:    
    def helpMsg(self):
        print("\nAdmin Menu:")
        print("(c) Clear Database File")
        print("(g) Group Students by Grade")
        print("(p) Partition Students by Pass/Fail")
        print("(r) Remove a Student")
        print("(s) Show All Students")
        print("(x) Exit to Main Menu")
        self.getUserInput()

""" admin main menu """
def adminMenu(self):
    choice = getInput("Start menu(c/g/p/r/s/x):")
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
                print("Unavailable option. You can input 'h' to show more detail.")
        choice = getInput("Start menu(c/g/p/r/s/x):") # 更新一次 user input
    print("Returning to main menu...")
    return
    