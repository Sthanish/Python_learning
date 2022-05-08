balance = 10000
curr_balance = 50000
print("Welcome to this atm")


def entry():
    username = input("Enter you atm username:")
    if username == 'anish':
        mypass()
    else:
        print("Incorrect username\nTry again")
        entry()


def mypass():
    pin = input("Enter your 4 digit transaction pin:")
    if pin == '1234':
        option()
    else:
        print("Incorrect password\ntry again")
        mypass()


def option():
    print("\n\nselect the account you want to access")
    choice = input("\n\n1.Current Account\n2.Saving Account\n3.exit\nenter a number:")
    print("\n\n")
    if choice == '1':
        user = Account(1)
        user.current()
    elif choice == '2':
        user = Account(2)
        user.saving()
    elif choice == '3':
        exit()
    else:
        print("Input Invalid")
        option()


class Account:
    def __init__(self, account_type):
        self.account_type = account_type

        if self.account_type == 1:
            self.user_info = Information(1)
        elif self.account_type == 2:
            self.user_info = Information(2)

    # current action
    def current(self):
        value = input("\n\n1.View balance\n2.withdraw cash\n3.Deposit cash\n4.Exit\nEnter one choice:")
        if value == '1':
            self.user_info.view_balance()
        elif value == '2':
            self.user_info.withdraw()
        elif value == '3':
            self.user_info.deposit()
        elif value == '4':
            option()
        else:
            print("Input Invalid")
            self.current()

    # saving action
    def saving(self):
        value = input("\n\n1.View balance\n2.withdraw cash\n3.Deposit cash\n4.Exit\nEnter one choice:")
        if value == '1':
            self.user_info.view_balance()
        elif value == '2':
            self.user_info.withdraw()
        elif value == '3':
            self.user_info.deposit()
        elif value == '4':
            option()
        else:
            print("Input Invalid")
            self.saving()


class Information:
    def __init__(self, account_type):
        self.account_type = account_type
        # global my_balance
        if self.account_type == 1:
            self.my_balance = curr_balance
        elif self.account_type == 2:
            self.my_balance = balance

    def view_balance(self):
        print("\n\nDear Customer you have Rs", self.my_balance, "in your account")

    def withdraw(self):
        try:
            cash = int(input("\n\nEnter the amount you want to withdraw: RS."))
            total = self.my_balance - cash
            print("\nDear Customer you have withdraw Rs.", cash)
            print("\nNow total balance is", total)
        except ValueError as ex:
            print(ex)
            print("\n\nInput invalid\nenter the amount:")
            self.withdraw()

    def deposit(self):
        try:
            cash = int(input("\n\nEnter the amount you want to deposit:RS."))
            total = self.my_balance + cash
            print("\nDear Customer you have deposit Rs.", cash, )
            print("\nNow, total balance is", total)
        except ValueError as ex:
            print(ex)
            print("\n\nInput invalid\nenter the amount:")
            self.deposit()
        # else:
        #     print("Something Went Wrong")
        # finally:
        #     exit()


entry()
