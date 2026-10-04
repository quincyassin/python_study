class BankAccount():

    bank_name = "宇宙银行"

    def __init__(self, owner: str, balance: float=0):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError("余额不能小于0")
        self._balance = balance

    def deposit(self, amount):
        self.balance+= amount

    def withdraw(self, amount):
        self.balance-= amount

    def __str__(self):
        return f"{self.bank_name}-账户：{self._owner}，余额：{self.balance}"

class SavingsAccount(BankAccount):

    bank_name = "宇宙银行-储蓄账户"

    def __init__(self, owner: str, balance: float=0):
        super().__init__(owner, balance)
        self.rate = 0.03

    def add_interest(self):
        self.balance+= self.balance * self.rate

bank_account = BankAccount("张三", 1000)
bank_account.deposit(500)
bank_account.withdraw(10)
print(bank_account)

savings_account = SavingsAccount("李四", 1000)
savings_account.deposit(500)
savings_account.add_interest()
print(savings_account)
