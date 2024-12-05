class BankAccount:
    def __init__(self, account_holder, balance=0):
        """Initialize account with holder's name and starting balance."""
        self.account_holder = account_holder   # public attribute
        self._balance = balance                # protected attribute

    def deposit(self, amount):
        """Add amount to balance."""
        if amount > 0:
            self._balance += amount
            print(f"{amount} deposited. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw amount if sufficient balance."""
        if amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn. New balance: {self._balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        """Get current balance."""
        return self._balance

# --- INHERITANCE & POLYMORPHISM ---
class SavingsAccount(BankAccount):
    """Savings account inherits from BankAccount, with an interest rate."""

    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        # Call superclass (BankAccount) constructor
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        """Calculate interest and add to balance."""
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest added at rate {self.interest_rate * 100}%: {interest}")

class CheckingAccount(BankAccount):
    """Checking account inherits from BankAccount, with an overdraft limit."""

    def __init__(self, account_holder, balance=0, overdraft_limit=500):
        # Call superclass (BankAccount) constructor
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Allow overdraft up to a certain limit."""
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            print(f"{amount} withdrawn (with overdraft). New balance: {self._balance}")
        else:
            print("Exceeded overdraft limit.")

# --- ENCAPSULATION ---
class Bank:
    """Bank manages multiple accounts."""

    def __init__(self):
        self._accounts = {}  # private attribute to store accounts

    def open_account(self, account_type, account_holder, **kwargs):
        """Open a new account (either savings or checking)."""
        if account_type == 'savings':
            account = SavingsAccount(account_holder, **kwargs)
        elif account_type == 'checking':
            account = CheckingAccount(account_holder, **kwargs)
        else:
            raise ValueError("Invalid account type")
        
        self._accounts[account_holder] = account
        print(f"Account for {account_holder} opened.")

    def get_account(self, account_holder):
        """Retrieve an account by holder's name."""
        return self._accounts.get(account_holder, None)

# --- ABSTRACTION ---
class TransactionProcessor:
    """Handles transactions with minimal knowledge of account details."""
    
    @staticmethod
    def process_deposit(account, amount):
        """Deposit money into account."""
        account.deposit(amount)

    @staticmethod
    def process_withdrawal(account, amount):
        """Withdraw money from account."""
        account.withdraw(amount)


# --- MAIN EXECUTION (Demonstrating OOP concepts) ---
if __name__ == "__main__":
    # Creating a bank instance
    bank = Bank()

    # Opening different types of accounts
    bank.open_account('savings', 'Alice', balance=1000, interest_rate=0.03)
    bank.open_account('checking', 'Bob', balance=500, overdraft_limit=300)

    # Accessing accounts
    alice_account = bank.get_account('Alice')
    bob_account = bank.get_account('Bob')

    # Demonstrating polymorphism: calling withdraw on different account types
    TransactionProcessor.process_deposit(alice_account, 500)
    TransactionProcessor.process_withdrawal(bob_account, 700)

    # Applying specific operations on account types
    alice_account.add_interest()  # Specific to SavingsAccount
    bob_account.withdraw(200)     # Specific overdraft behavior in CheckingAccount

    # Encapsulation: Trying to access a private attribute directly will raise an error
    try:
        print(bank._accounts)  # Should not be accessed directly
    except AttributeError as e:
        print(f"Error: {e}")
