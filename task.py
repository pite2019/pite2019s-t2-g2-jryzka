class Bank():
        def __init__(self, name, stat):
                self.client_name = name
                self.account_status = stat
        def withdraw(self, how_much):
                self.account_status = self.account_status - how_much
        def cash_input(self,  money_input):
                self.account_status = self.account_status + money_input

class ClientAccount(Bank):
        def __init__(self, name, stat):
                self.client_name = name
                self.account_status = stat
        def transfer(self, trans, Bank):
                Bank.account_status = Bank.account_status + trans
                self.account_status = self.account_status - trans



bank = Bank("Kowalski", 1000)
bank2 = Bank("Dom", 1500)
bank3 = ClientAccount("HH", 1000)
print(bank3.account_status)
bank3.account_status = 1500
bank3.transfer(200, bank)
print(bank3.client_name)
#bank.cash_input(150)
print(bank.account_status)

