import re

def getInput(prompt: str) -> str:
    return input(prompt).strip().lower()

""" validator """
"""valid email"""
def validate_email(email):
    pattern = re.compile(r"^[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com$")
    return pattern.match(email) is not None

""" valid password """
def validate_password(password):
    pattern = re.compile(r"^[A-Z][a-zA-Z]{5,}[0-9]{3,}$")
    return pattern.match(password) is not None