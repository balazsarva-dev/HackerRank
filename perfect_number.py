import logging
import re

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Calling '{func.__name__}' func with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Returned: {result}")
        return result
    return wrapper

def get_valid_number(prompt: str, min_limit: int, max_limit: int) -> int:
    while True:
        try:
            number = int(input(prompt))
            if number in range(min_limit, max_limit + 1):
                return number
            else:
                logger.warning(f"Out of range error! Please try again from {min_limit} and {max_limit}! ")
        except ValueError:
            logger.error("Invalid input! Please enter a number! ")

@logging_decorator
def perfect_number(n: int) -> bool:
    return sum(i for i in range(1, n//2 + 1) if n % i == 0) == n

@logging_decorator
def valid_password(password: str, min_length: int, max_lenght: int) -> bool:
    if len(password) not in range(min_length, max_lenght + 1):
        return False
    patterns = [r'[0-9]', r'[a-z]', r'[A-Z]', r'[@$!%*?&]']
    for pattern in patterns:
        if not re.search(pattern, password):
            return False
    return True

def main():
    options = {0: "Perfect number", 1: "Valid password"}
    get_option = get_valid_number(f"Enter 0 if you want to test the Perfect number function or 1 if the Valid Password: ", *options.keys())
    test_iteration_number = get_valid_number("Enter the number of tests you would run: ", min_limit=1, max_limit=10)
    for i in range(test_iteration_number):
        logger.info(f"Test #{i + 1}")
        if get_option == 0:
            test_number = get_valid_number("Enter a number: ", min_limit=1, max_limit=10**6)
            logger.info(f"Valid number: {test_number}")
            perfect_number(test_number)
        else:
            password = input("Enter a password: ")
            logger.info(f"Valid password: {password}")
            valid_password(password, min_length=8, max_lenght=20)

if __name__ == "__main__":
    main()