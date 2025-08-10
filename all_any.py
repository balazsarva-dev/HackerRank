from typing import List
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='basic_config.log', level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

def get_valid_number(min_value: int, max_value: int) -> int:
    while True:
        try:
            value = int(input(f'Set a value between {min_value} and {max_value}! '))
            logger.info(f'You entered {value}. ')
            if value in range(min_value, max_value+1):
                return value
            else:
                logger.warning(f'Out of range! Enter a number between {min_value} and {max_value}! ')
        except ValueError:
            logger.error('Missing or invalid input! Try again! ')

def get_integer_values(expected_length: int) -> List[int]:
    while True:
        values = input(f'Create a list! Its length must be {expected_length}! ').split()
        if len(values) != expected_length:
            logger.warning(f'Invalid number of elements! It must contain {expected_length} values! Try again! ')
            continue
        try:
            int_values = list(map(int, values))
            return int_values
        except ValueError:
            logger.error('Missing or invalid input! Every value must be integer! Try again! ')

def check_conditions(values_of_a_list: List[int]) -> bool:
    first_conditional = all(num >= 0 for num in values_of_a_list)
    second_conditional = any(str(value) == str(value)[::-1] for value in values_of_a_list)
    return all([first_conditional, second_conditional])

def main():
    N = get_valid_number(1, 10)
    values = get_integer_values(N)
    return check_conditions(values)
    
if __name__ == '__main__':
    result = main()
    print(result)