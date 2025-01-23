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
    def __init__(self):
        self.balance=100
        print("Hello! Welcome to the ATM Depot!")
    
    def authenticate(self):
        while True:
            pin = int(input("Enter account pin: "))
            if pin != 1234:
                logger.error("Error! Invalid pin. Try again.")
            else:
                return None

    def deposit(self):
        try:
            amount=float(input("Enter amount to be deposited: "))
            if amount < 0:
                logger.warning("Warning! You entered a negative number to deposit.")
            self.balance += amount
            logger.info("Amount Deposited: $%s\nTransaction Info:\nStatus: Successful\nTransaction #%s\nTimestamp: %s",
            amount, random.randint(10000, 1000000), datetime.now())
            
        except ValueError:
            logger.error("Error! You entered a non-number value to deposit.")
            logger.info("Transaction Info:\nStatus: Failed\nTransaction #%s\nTimestamp: %s",
            amount, random.randint(10000, 1000000), datetime.now())

    def withdraw(self):
        try:
            amount = float(input("Enter amount to be withdrawn: "))
            if self.balance >= amount:
                self.balance -= amount
                logger.info("You withdrew: $%s\nTransaction Info:\nStatus: Successful\nTransaction #%s",
                amount, random.randint(10000, 1000000))
            else:
                logger.error("Error! Insufficient balance to complete withdraw.\nTransaction Info:\nStatus: Failed\nTransaction #%s",
                random.randint(10000, 1000000))
        except ValueError:
            logger.error("Error! You entered a non-number value to withdraw.\nTransaction Info:\nStatus: Failed\nTransaction #%s\nTimestamp: %s",
            random.randint(10000, 1000000), datetime.now())

    def display(self):
        print("Available Balance = $", self.balance)

acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()