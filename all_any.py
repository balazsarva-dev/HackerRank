from typing import List
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

def get_valid_number(min_value: int, max_value: int) -> int:
    while True:
        try:
            value = int(input(f'Set a value between {min_value} and {max_value}! '))
            if value in range(min_value, max_value+1):
                return value
            logger.error(f'Out of range! Enter a number between {min_value} and {max_value}! ')
        except ValueError:
            logger.critical('Missing or invalid input! Try again! ')
            
def get_integer_values(expected_length: int) -> List[int]:        
    while True:
        values = input(f'Create a list! Its length must be {expected_length}! ').split()
        if len(values) != expected_length:
            logger.error(f'Invalid number of elements! It must contain {expected_length} values! Try again! ')
            continue
        try:
            int_values = list(map(int, values))
            return int_values
        except ValueError:
            logger.critical('Missing or invalid input! Every value must be integer! Try again! ')
            
def check_conditions(values: List[int]) -> bool:
    first_conditional = all(num >= 0 for num in values)
    second_conditional = any(str(value) == str(value)[::-1] for value in values)
    return all([first_conditional, second_conditional])

def main():
    N = get_valid_number(1, 10)
    values = get_integer_values(N)
    print(check_conditions(values))

if __name__ == '__main__':
    main()