class Bank_open():
    def __init__(self,name) :
        self.name=name
        print("welcome",self.name)
        

    @staticmethod
    def is_open(day):
        if day != "sunday":
            print("Bank is open")
        else:
            print("Bank is not open")

# you dont need to creat an object to access a static method
# ab=Bank_open("Abdullah")    


Bank_open.is_open("sunday")
Bank_open.is_open("monday")