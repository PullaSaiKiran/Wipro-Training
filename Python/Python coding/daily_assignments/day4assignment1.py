# Use class, objects, constructors while coding
# Bank Account Management System
# You are tasked with creating a simple bank account management system in Python.
# Implement a class called BankAccount with the following specifications:
# The class should have private instance variables for account number, account holder
# name, and balance.
# Include a constructor to initialize these variables.
# Implement getter and setter methods for each instance variable to ensure
# encapsulation.
# Implement methods to deposit and withdraw money from the account.
# Ensure that the withdraw method checks if the account has sufficient balance before
# allowing withdrawal.
# Write a Python program to demonstrate the functionality of the BankAccount class by
# creating instances, depositing and withdrawing money, and displaying account
# information.

class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    @property
    def get_account_number(self):
        return self.__account_number

    def get_holder_name(self):
        return  self.__holder_name

    def get_balance(self):
        return self.__balance


    def set_account_number(self,account_number):
        self.__account_number = account_number

    def set__holder_name(self,holder_name):
        self.__holder_name=holder_name

    def set_balance(self,balance):
        if balance >=0:
            self.__balance = balance
        else:
            print("Insufficient Balance ")


    def deposit(self,amount):
        if amount> 0:
            self.__balance +=amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount>0:
            if self.__balance >= amount:
                self.__balance -=amount
                print(f"Withdrew {amount}. New balance: {self.__balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive.")

    def display_info(self):
        print("\n Account Information ")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__holder_name}")
        print(f"Balance: {self.__balance}")


def main():
    # Create account dynamically
    acc_no = int(input("Enter Account Number: "))
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))
    account = BankAccount(acc_no, name, balance)

    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Account Info")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == 2:
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == 3:
            account.display_info()
        elif choice == 4:
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
