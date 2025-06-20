class BankAccount:
    def __init__(self):
        self.__balance = 0

    def withdraw(self, amount):
        self.__balance -= amount
        print("통장에 %d가 출금되었습니다." %amount)
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("통장에서 %d가 입금되었습니다." %amount)
        return self.__balance

    def get_balance(self):
        return self.__balance

a = BankAccount()

while True:
    menu = input("메뉴를 선택( 1: 입금, 2: 출금, 3: 종료):")
    if menu == '1':
        a.deposit(int(input("입금할 금액을 입력하세요:")))
        print("당신의 계좌의 잔액:", a.get_balance())
    elif menu == '2':
        a.withdraw(int(input("출금할 금액을 입력하세요:")))
        print("당신의 계좌의 잔액:", a.get_balance())
    elif menu == '3':
        print("종료합니다.")
        break
    else:
        print("메뉴는 1과 2만 선택할 수 있습니다. \n다시 선택해주세요.")
