import random

class Bank():
    random_num=random.randint(11111,99999)
    def __init__(self):
        print()
        print("Wellcome to Bank")
        self.menu()

    def menu(self):
        print("""
        Press Button => 
        1 : Creat a new Saving Account
        2 : Access an Existing one
        3 : Exit
        """)
    
        input_1=int(input("Enter => "))
        if input_1==1:
            self.creat_account()
        elif input_1==2:
            self.access_account()
        elif input_1==3:
            exit()
        else:
            print("invalid Input !")
            self.menu()
    


    def creat_account(self):
        name=input("Enter your Name : ")
        balance=int(input("Enter your balance : "))
        account_number=Bank.random_num
        print("% Account created %")
        print("Your Account no is",account_number)

        self.name=name
        self.balance=balance
        self.account_number=account_number

        self.menu()

 
    def access_account(self):
 
        given_name=input("Enter your name : ")
        given_account_no=int(input("Enter your account number : "))

        if given_name==self.name and given_account_no==self.account_number:
            print("% ACCOUNT ACCESS GRANTED %")
            self.access_menu()        
        else:
            print("INVALID CRIDANTIALS ! ")
            self.menu()


    def access_menu(self):
        print("""
        Press Button => 
        1 : Withdraw Money
        2 : Deposit Money
        3 : Check balance
        4 : Exit
        """)
        input_2=int(input("Enter => "))
        if input_2==1:
            self.withdraw()
        elif input_2==2:
            self.deposit()
        elif input_2==3:
            self.check_balace()
        elif input_2==4:
            exit()
        else:
            print("invalid Input !")
            self.access_menu()


    def withdraw(self):
        amount_withdraw= int(input("Enter Withdraw amount : "))
        if amount_withdraw<self.balance:
            self.balance = self.balance - amount_withdraw
            print("% Withdraw Completed %")
            self.access_menu()
        else:
            print("Invalid Balance !")
            self.access_menu()


    def deposit(self):
        amount_deposit = int(input("Enter deposit amount : "))
        self.balance = self.balance + amount_deposit
        print("% Deposit Completed %")
        self.access_menu()


    def check_balace(self):
        print("Your balance is",self.balance)
        self.access_menu()



if __name__=='__main__':
    user=Bank()