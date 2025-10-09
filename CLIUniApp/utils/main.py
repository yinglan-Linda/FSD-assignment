class userLogin:
    def __init__(self, name, password):
        userName = input("Enter your name:")
        password = input("Enter your password:") 
        try:
            userName == "admin"
        except ValueError:
            print()
        finally:
            print(f"Welcome, {name}!")


class studentSystem:
    def __init__(self, name): # Initial value
        super().__init__(self, name)
        self.name = name
        # self.balance = 0.0

    
    def getUserInput(self):
        self = input("Start banking(d/w/s/x):").strip().lower()

    def helpMsg(self):
        print("d - deposit /n w - withdraw /n s - show balance")
        studentSystem.getUserInput(self)


def main():
    
    # account = BankAccount(name)
    # account.login()
    # account.save_money()
    # print("Start banking(d/w/s/x):")

    user_input = input("Start banking(d/w/s/x):").strip().lower()
    # print("Starting balance is ", account.getInitBalance)

    account = studentSystem(user_input)

    # user_input = account.getInitBalance()
    while (user_input != 'x'):
        match user_input:
            case 'd':
                account.deposit()
            case 'w':
                account.withdraw()
            case 's':
                account.showBalance()
                # user_input = input("Start banking(d/w/s/x):").strip().lower()
            case 'h':
                account.helpMsg()
            case _:
                print("Available options (d/w/s/w). You can input 'h' to show more detail.")

    # user_input = account.getInitBalance()
    print("Thank you for your using.")
            

if __name__ == "__main__":
    main()