import random
import logging
import sys
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)
formatter_stream = logging.Formatter('[%(asctime)s] - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter_stream)
logger.addHandler(stream_handler)
file_handler = logging.FileHandler("formatted.log")
logger.addHandler(file_handler)

class BankAccount:
    transactions = 0
    attempts = 0
    
    def __init__(self):
        self.balance=100
        logger.info("Hello! Welcome to the ATM Depot! ")
    
    def authenticate(self):
        MAX_ATTEMPTS = 3
        while MAX_ATTEMPTS > 0:
            pin = int(input("Enter your pin: "))
            if pin == 1234:
                logger.info("Authentication successful! ")
                return
            else:
                logger.error("Invalid pin. You have %s attempts left. Try again! ", MAX_ATTEMPTS - 1)
                MAX_ATTEMPTS -= 1
        logger.error("Maximum attempts reached. Exiting program.")
        raise SystemExit

    def deposit(self):
        try:
            amount=float(input("Enter amount to be deposited: "))
            if amount < 0:
                logger.warning("You entered a negative number to deposit. Try again! ")
                BankAccount.attempts += 1
            BankAccount.transactions += 1
            self.balance += amount
            logger.info("Amount Deposited: $%s\nTransaction Info:\nStatus: Successful\nTransaction #%s\nTimestamp: %s",
            amount, BankAccount.transactions, datetime.now())
            
        except ValueError:
            logger.error("Error! You entered a non-number value to deposit.")
            BankAccount.attempts += 1
            logger.info("Transaction Info:\nStatus: Failed\nTransaction #%s\nTimestamp: %s",
            BankAccount.transactions, datetime.now())

    def withdraw(self):
        try:
            amount = float(input("Enter amount to be withdrawn: "))
            if self.balance >= amount:
                self.balance -= amount
                BankAccount.transactions += 1
                logger.info("You withdrew: $%s\nTransaction Info:\nStatus: Successful\nTransaction #%s",
                amount, BankAccount.transactions)
            else:
                logger.error("Error! Insufficient balance to complete withdraw.\nTransaction Info:\nStatus: Failed\nTransaction #%s",
                BankAccount.transactions)
        except ValueError:
            logger.error("Error! You entered a non-number value to withdraw.\nTransaction Info:\nStatus: Failed\nTransaction #%s\nTimestamp: %s",
            random.randint(10000, 1000000), datetime.now())

    def display(self):
        logger.info("Available Balance = $", self.balance)

acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()