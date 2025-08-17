# -*- coding: utf-8 -*-
class BankAccount:
    def __init__(self, name): # Initial value
        self.name = name
        self.balance = 0.0

    def login(self):
        print("Enter your password:")
        password = input() 
        print(f"Welcome, {self.name}!")

    def save_money(self):
        print("Save money:")
        amount = float(input()) # ensure float number
        self.balance += amount
        print(f"Now your money is ${self.balance:.2f}") # keep two decimal places

def main():
    print("Enter your name:")
    name = input()
    account = BankAccount(name)
    account.login()
    account.save_money()

if __name__ == "__main__":
    main()