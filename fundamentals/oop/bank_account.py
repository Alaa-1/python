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


# Create 2 accounts

first_account = BankAccount(2, 45000)
second_account = BankAccount(3, 9999999)

# To the first account, make 3 deposits and 1 withdrawal,
# then yield interest and display the account's info all in one line of code (i.e. chaining)

first_account.deposit(200).deposit(7000).deposit(
    1
).yield_interest().display_account_info()


# To the second account,
# make 2 deposits and 4 withdrawals,
# then yield interest and display the account's info all in one line of code (i.e. chaining)


second_account.deposit(10).deposit(300000).withdraw(47500).withdraw(800000).withdraw(
    100
).withdraw(731000).yield_interest().display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info

BankAccount.all_accounts_info()
