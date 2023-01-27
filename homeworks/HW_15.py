# 1. Write a Python class named Circle constructed by a radius
# and two methods which will compute the area and the perimeter of a circle.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * 3.14 * self.radius


circle = Circle(3)
print(f"The area of a circle with radius={circle.radius} is {circle.area}, the perimeter is {circle.perimeter}")


# 2. Write a Python program to crate two empty classes, Student and Marks.
# Now create some instances and check whether they are instances of the said classes or not.
# Also, check whether the said classes are subclasses of the built-in object class or not.


class Student:
    pass


class Marks:
    pass


student1 = Student()
mark1 = Marks()
print(f"student1 is instance of class Student: {isinstance(student1, Student)}")
print(f"student1 is instance of class Marks: {isinstance(student1, Marks)}")
print(f"mark1 is instance of class Student: {isinstance(mark1, Student)}")
print(f"mark1 is instance of class Marks: {isinstance(mark1, Marks)}")

print(f"Class Student is subclass of the built-in object class: {issubclass(Student, object)}")
print(f"Class Marks is subclass of the built-in object class: {issubclass(Marks, object)}")


# 3. A Bank
class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


# A. Using the Account class as a base class, write two derived classes
# called SavingsAccount and CurrentAccount.
# A SavingsAccount object, in addition to the attributes of an Account object,
# should have an interest attribute and a method which adds interest to the account.
# A CurrentAccount object, in addition to the attributes of an Account object,
# should have an overdraft limit attribute.


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self._interest = interest

    def get_interest(self):
        return self._interest

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}, interest: {self._interest}'


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit


# B. Now create a Bank class, an object of which contains an array of Account objects.
# Accounts in the array could be instances of the Account class, the SavingsAccount class,
# or the CurrentAccount class. Create some test accounts (some of each type).

class Bank():
    def __init__(self, accounts: list[Account | SavingsAccount | CurrentAccount]):
        self.accounts = accounts


acc = [
    Account(4_000, 123),
    SavingsAccount(5_000, 125, 0.5),
    CurrentAccount(-7_000, 158, -5_000),
]

bank = Bank(accounts=acc)


# C. Write an update method in the Bank class. It iterates through each account,
# updating it in the following ways: Savings accounts get interest added
# (via the method you already wrote); CurrentAccounts get a letter sent if they are in overdraft.
# (use print to 'send' the letter).


class Bank():
    def __init__(self, accounts: list[Account | SavingsAccount | CurrentAccount]):
        self.accounts = accounts

    def update(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                print(f"Account {account._account_number}: interest = {account.get_interest()}")
            if isinstance(account, CurrentAccount):
                if account._balance < account._overdraft_limit:
                    print(f"Account {account._account_number}: You are in overdraft")
        return


bank = Bank(accounts=acc)
bank.update()

# D. The Bank class requires methods for opening and closing accounts,
# and for paying a dividend into each account.


class Bank():

    def __init__(self, accounts: list[Account | SavingsAccount | CurrentAccount]):
        self.accounts = accounts

    def open_account_in_bank(self):
        type = input("Input type of account, You want to create (Current, Savings): ")

        match type:
            case "Current":
                account_number = input("Input account number: ")
                account_balance = input("Input account balance: ")
                overdraft_limit = input("Input limit of overdtaf: ")
                account = CurrentAccount(account_number=account_number,
                                         balance=account_balance,
                                         overdraft_limit=overdraft_limit)
                print("!!! ACCOUNT CREATED SUCCESSFYLLY !!!")
            case "Savings":
                account_number = input("Input account number: ")
                account_balance = input("Input account balance: ")
                interest = input("Input interest: ")
                account = SavingsAccount(account_number=account_number,
                                         balance=account_balance,
                                         interest=interest)
                print("!!! ACCOUNT CREATED SUCCESSFYLLY !!!")
            case _:
                return 'Type of account must be "Current" or "Savings"'

        self.accounts.append(account)
        return

    def close_account_in_bank(self):
        account_number = int(input("Input account number You want to closing: "))
        for account in self.accounts:
            if account._account_number == account_number:
                print("!!! ACCOUNT CLOSED SUCCESSFYLLY !!!")
                self.accounts.remove(account)
        return

    def paying_dividend(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account._balance = round(float(account._balance) * (1 + float(account._interest)/100), 2)
                print(f"Dividends credited to the savings account {account._account_number}, new balance: {account._balance}")
        return

    def __str__(self):
        out = ""
        for acc in self.accounts:
            out += (f'\nAccount: {acc._account_number} with balanse {acc._balance}')
        return out


bank = Bank(acc)
print(bank)

bank.open_account_in_bank()
print(bank)

bank.close_account_in_bank()
print(bank)

bank.paying_dividend()
print(bank)
