import admin_system
import student_system
import utils.utils as utils
from controller.student_controller import StudentController
from controller.admin_controller import AdminController
from colorama import init, Fore
init(autoreset=True)   # 打印一次颜色后自动复位，避免后面整行都被染色

""" main entrance """
def main():
    
    studentCtrl = StudentController()  # 初始化学生控制器
    print("Welcome to university!")
    role = utils.getInput("University system: (a)admin/ (s)student/ (x)Exit>")

    while (role != 'x'):
        match role:
            case 'a':
                # admin = admin_system.AdminSystem() # 创建实例
                # admin_system.adminMenu(admin) #把实例传入admin_system
                admin = admin_system.AdminSystem(AdminController())  # 传入实例
                admin.run()                                          # 调实例方法
            case 's':                
                student = student_system.StudentSystem(studentCtrl) # 创建实例
                student.run() #把实例传入student_system
            case _:
                utils.infoMSG("Unavailable option.")
                # print("Unavailable option. You can input 'h' to show more detail.")
        role = utils.getInput("University system: (a)admin/ (s)student/ (x)Exit>") # 更新一次 user input

    utils.infoMSG("Thank you.")
    # print(Fore.YELLOW + "Thank you.")

if __name__ == "__main__":
    main()