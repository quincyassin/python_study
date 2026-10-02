class BankAccount():
    def __init__(self, owner: str, balance: float=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance+= amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("余额不足")
            return None
        self.balance-= amount

    def __str__(self):
        return f"账户：{self.owner}，余额：{self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float=0):
        super().__init__(owner, balance)
        self.rate = 0.03

    def add_interest(self):
        self.balance+= self.balance * self.rate

bank_account = BankAccount("张三", 1000)
bank_account.deposit(500)
bank_account.withdraw(200)
print(bank_account)

savings_account = SavingsAccount("李四", 1000)
savings_account.deposit(500)
savings_account.add_interest()
print(savings_account)
