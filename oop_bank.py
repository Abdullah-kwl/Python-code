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
        else:
            print("INVALID CRIDANTIALS ! ")
            self.menu()




user=Bank()