class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    # deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    # make withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    # display user balance method
    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self

    def transfer_money(from_account, to_account, amount):
        from_account.make_withdrawal(amount)
        to_account.make_deposit(amount)


# Create 3 instances of the User class

vi = User("Vi", "vi@lemail.com")
george = User("George", "geohotz@rel.fr")
robin = User("Robin", "robin.sanders@crypto.co.uk")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance

vi.make_deposit(3500).make_deposit(700).make_deposit(1000).make_withdrawal(
    800
).display_user_balance()
# vi.make_deposit(700)
# vi.make_deposit(1000)

# vi.make_withdrawal(800)

# vi.display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance

george.make_deposit(86000).make_deposit(9020).make_withdrawal(
    15000
).display_user_balance()
# george.make_deposit(9020)
# george.make_withdrawal(15000)

# george.display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance

robin.make_deposit(51900).make_withdrawal(3575).make_withdrawal(4770).make_withdrawal(
    9999
).display_user_balance()

# robin.make_withdrawal(3575)
# robin.make_withdrawal(4770)
# robin.make_withdrawal(9999)

# robin.display_user_balance()

# BONUS: Add a transfer_money method;
# have the first user transfer money to the third user and then print both users' balances

User.transfer_money(vi, robin, 4000)
print("After Transfer: ")
vi.display_user_balance()
robin.display_user_balance()
