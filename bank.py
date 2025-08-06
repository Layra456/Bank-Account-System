class BankAccount:
    Bank_name = "Arham bank Limited"

    def __init__(self, name, Balance):
        self.name = name
        self.__Balance = Balance

    def deposit(self, amount):
        if amount >= 500:
            self.__Balance += amount
            print(f"The {amount} pkr is Added to {self.name}'s Account")
        else:
            print(f"This {amount} is insufficient for deposit in {self.name}")
            print(f"Amount must be >=500 pkr")

    def withdraw(self, amount):
        if 500 <= amount <= self.__Balance:
            self.__Balance -= amount
            print(f"The {amount} pkr is deduct from {self.name}'s Account")
        else:
            print(f"This {amount} is insufficeint for withdraw")
            print(f"Amount must be >=500 pkr")

    def get_balance(self):
        return self.__Balance

    def show_detail(self):
        print(f"Account holder : {self.name}")
        print(f"Current Balance : {self.get_balance()}")

    @staticmethod
    def bank_detail():
        print(f"Welcome to {BankAccount.Bank_name}")


BankAccount.bank_detail()

account1 = BankAccount(name=input('Enter your Name :'),
                       Balance=int(input("Enter your Balance : ")))
account1.show_detail()

account1.deposit(amount=int(input("Enter the amount you wanna deposit : ")))
account1.withdraw(amount=int(input("Enter the amount you wanna withdraw : ")))

account1.show_detail()
