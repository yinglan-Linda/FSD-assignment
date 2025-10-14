import admin_system
import student_system
from utils.utils import getInput

""" main entrance """
def main():
    print("Welcome to university!")
    role = getInput("Choose your role \n(a)admin\n(s)student\n(x)Exit\n>")

    while (role != 'x'):
        match role:
            case 'a':
                admin = admin_system.AdminSystem() # 创建实例
                admin_system.adminMenu(admin) #把实例传入admin_system
            case 's':
                student = student_system.StudentSystem() # 创建实例
                student_system.studentMenu(student) #把实例传入student_system
                pass
            case _:
                print("Unavailable option. You can input 'h' to show more detail.")
        role = getInput("Choose your role \n(a)admin\n(s)student\n(x)Exit\n>") # 更新一次 user input

    print("Goodbye.")

if __name__ == "__main__":
    main()