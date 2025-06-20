class BankAccount:
    def __init__(self, name, number, balance):
        self.balance= balance
        self.name = name
        self.number= number
    def withdraw(self, amount):
        self.balance-= amount
        return self.balance
    def deposit(self, amount):
        self.balance+= amount
        return self.balance

class SavingsAccount(BankAccount) :
    def __init__(self,  name, number, balance,  interest_rate):# 금리
        super().__init__( name, number, balance)
        self.interest_rate=interest_rate
    def set_interest_rate(self, interest_rate):
        self.interest_rate= interest_rate
    def get_interest_rate(self):
        return self.interest_rate
    def add_interest(self):# 예금에이자를더한다.
        self.balance+= self.balance*self.interest_rate


class CheckingAccount(BankAccount) :
    def __init__(self,  name, number, balance):
        super().__init__( name, number, balance)
        self.withdraw_charge= 10000# 수표발행수수료
    def withdraw(self, amount):
        return BankAccount.withdraw(self, amount + self.withdraw_charge)
    
a1 = SavingsAccount("홍길동", 123456, 10000, 0.05)
a1.add_interest()
print("저축예금의잔액=", a1.balance)

a2 = CheckingAccount("김철수", 123457, 2000000)
a2.withdraw(100000)
print("당좌예금의잔액=", a2.balance)
