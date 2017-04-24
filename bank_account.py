class BankAccount:
    def deposit(self):
        pass

    def withdraw(self):
        pass


class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 500

    def deposit(self, deposit):
        if deposit < 0:
            return 'Invalid deposit amount'

        else:
            self.balance += deposit
        return self.balance

    def withdraw(self, withdrawal):
        bal = self.balance - withdrawal
        if withdrawal < 0:
            return 'Invalid withdraw amount'
        elif withdrawal > self.balance:
            return 'Cannot withdraw beyond the current account balance'
        elif bal < 500:
            return 'Cannot withdraw beyond the minimum account balance'
        else:
            self.balance -= withdrawal
        return self.balance


class CurrentAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, deposit):
        if deposit < 0:
            return 'Invalid deposit amount'

        else:
            self.balance += deposit
        return self.balance

    def withdraw(self, withdrawal):
        if withdrawal < 0:
            return 'Invalid withdraw amount'
        elif self.balance < withdrawal:
            return 'Cannot withdraw beyond the current account balance'
        else:
            self.balance -= withdrawal
        return self.balance


sa = SavingsAccount()
print(isinstance(sa, BankAccount))
sa.deposit(2300)
print(sa.balance)
print(sa.withdraw(543))

ca = CurrentAccount()
print(isinstance(ca, BankAccount))
ca.deposit(23001)
print(ca.balance)
print(ca.withdraw(23002))
