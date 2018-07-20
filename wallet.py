class InsufficientAmount(Exception):
    pass


class InsufficientFundsException(Exception):
    pass


class Wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough balance to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount

    def transfer_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough balance to transfer {}'.format(amount))
        self.balance -= amount


class Banker:
    def __init__(self, total_amount=0):
        self.total = total_amount

    def giveLoan(self, loan_amount):
        if self.total >= loan_amount:
            self.total -= loan_amount
        else:
            raise InsufficientFundsException('Not enough balance to transfer {}'.format(loan_amount))

    def collectLoanAmount(self, payment):
        self.total += payment


