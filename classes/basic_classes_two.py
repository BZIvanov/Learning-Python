class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, account_name):
        self.balance = initial_amount
        self.name = account_name
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, '{self.name}' has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try: 
            print('\nBeginning Transfer')
            self.viable_transaction(amount) 
            self.withdraw(amount) 
            account.deposit(amount) 
            print('\nTransfer completed!')
        except BalanceException as error: 
            print(f'\nTransfer interrupted. {error}')


Iva = BankAccount(200, "Iva")
Moni = BankAccount(300, "Moni")

Iva.get_balance()
Moni.get_balance()

Iva.deposit(30)

Moni.withdraw(1000)
Moni.withdraw(10)

Moni.transfer(50, Iva)
