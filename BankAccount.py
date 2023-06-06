# create a class

class BankAccount:

    # constructor method, initialize your objects
    def __init__(self, account_number, account_holder, balance = 0) -> None:
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    # create object method
    def deposit(self, amount):
        self.balance += amount
        print(f'You deposited {amount}$. Your current balance is {self.balance}')
    
    # create object method
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'You withdrew {amount}$. Your current balance is {self.balance}')
        else:
            print(f'Sorry, you do not have sufficient funds to withdraw {amount}$. Your current balance is {self.balance}')
    

    # create object method
    def check_balance(self):
        print(f'Account Holder: {self.account_holder}')
        print(f'Account Number: {self.account_number}')
        print(f'Current Balance: {self.balance}')

account_1 = BankAccount('abc', 'John Doe')
account_2 = BankAccount('xyz', 'Jane Smith', 1001)

account_1.deposit(200)
account_1.withdraw(201)
account_1.check_balance()

# account_2.deposit(500)
# account_2.withdraw(100)
# account_2.check_balance()

# create account1, account2 objects
# account 1 starts with 1000 balance, account2 starts with 0 balance

# deposit 1000, withdraw 55, check balance for account1   
# deposit 550, withdraw 3, check balance for account2

# account1.deposit(1)