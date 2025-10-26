import re
from colorama import Fore,Style

# get user input
# get user input
def getInput(prompt: str) -> str:
    return input(f"{Fore.BLUE}" + prompt + Style.RESET_ALL).strip().lower()

""" validator """
"""valid email"""
def validateEmail(email):
    pattern = re.compile(r"^[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com$")
    return pattern.match(email) is not None

""" valid password """
def validatePassword(password):
    pattern = re.compile(r"^[A-Z][a-zA-Z]{5,}[0-9]{3,}$")
    return pattern.match(password) is not None

""" colorful message """
def infoMSG(msg): 
    print(f"{Fore.YELLOW}{msg}{Style.RESET_ALL}") # 黄色：提示信息
def errMSG(msg):
    print(f"{Fore.RED}{msg}{Style.RESET_ALL}")  # 红色：报错
def greenMSG(msg):
    print(f"{Fore.GREEN}{msg}{Style.RESET_ALL}")  # 绿色：当前状态