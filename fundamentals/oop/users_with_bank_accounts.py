class BankAccount:
    all_accounts = []

    def __init__(self, interest_rate=1, balance=0):
        self.interest_rate = interest_rate / 100
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance is {self.balance}$")
        return self

    def yield_interest(self):
        if BankAccount.is_positive(self.balance):
            self.balance *= self.interest_rate
        return self

    @staticmethod
    def is_positive(balance):
        if balance > 0:
            return True
        else:
            return False

    # NINJA BONUS
    @classmethod
    def all_accounts_info(cls):
        print("-" * 20)
        for account in cls.all_accounts:
            account.display_account_info()
        print("-" * 20)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest_rate=0.05, balance=9000)

    # deposit method
    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    # make withdrawal method
    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self

    # display user balance method
    def display_user_balance(self):
        print(self.name, self.account.balance)
        return self

    def transfer_money(from_account, to_account, amount):
        from_account.account.deposit(amount)
        to_account.account.withdraw(amount)

#TODO
#?SENSEI BONUS: Allow a user to have multiple accounts;
#?update methods so the user has to specify which account they are withdrawing or depositing to