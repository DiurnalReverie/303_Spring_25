import datetime
import string

# Part A: Encode function
def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)  # List of lowercase alphabet letters
    encoded_text = []
    for char in input_text:
        if char.isalpha():
            # Shift character within the alphabet
            new_char = chr(((ord(char.lower()) - ord('a') + shift) % 26) + ord('a'))
            encoded_text.append(new_char if char.islower() else new_char.upper())
        else:
            encoded_text.append(char)
    return alphabet, ''.join(encoded_text)

# Part B: Decode function
def decode(input_text, shift):
    decoded_text = []
    for char in input_text:
        if char.isalpha():
            # Shift character back within the alphabet
            new_char = chr(((ord(char.lower()) - ord('a') - shift) % 26) + ord('a'))
            decoded_text.append(new_char if char.islower() else new_char.upper())
        else:
            decoded_text.append(char)
    return ''.join(decoded_text)

# Part C: BankAccount Class
class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        if creation_date is None:
            self.creation_date = datetime.date.today()
        elif creation_date > datetime.date.today():
            raise Exception("Account creation date cannot be in the future")
        else:
            self.creation_date = creation_date
        self.name = name
        self.ID = ID
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def view_balance(self):
        return self.balance

# Part D: SavingsAccount Class (inherits BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        super().__init__(name, ID, creation_date, balance)

    def withdraw(self, amount):
        # Check if the account is at least 180 days old
        if (datetime.date.today() - self.creation_date).days < 180:
            print("Account must be at least 180 days old to withdraw.")
            return
        super().withdraw(amount)

# Part E: CheckingAccount Class (inherits BankAccount)
class CheckingAccount(BankAccount):
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        super().__init__(name, ID, creation_date, balance)

    def withdraw(self, amount):
        if self.balance - amount < 0:
            # Apply overdraft fee of $30
            self.balance -= 30
            print(f"Overdraft fee applied. New balance: {self.balance}")
        super().withdraw(amount)
