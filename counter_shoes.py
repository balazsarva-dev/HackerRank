from collections import Counter
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def get_valid_number(prompt: str, min_val: int, max_val: int) -> int:
    """
    Prompts the user for a valid integer within a specified range.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_val < value < max_val:
                logger.info(f"You entered a valid number: {value}")
                return value
            else:
                logger.warning(f"You entered an invalid number: {value}")
        except ValueError:
            logger.error('Only integer is allowed! Try again!')

def get_a_valid_list(length_of_list: int, min_value: int, max_value: int) -> list:
    """
    Prompts the user for a valid list of integers within a specified range.
    """
    while True:
        try:
            values = list(map(int, input(f'Enter the shoe sizes from ({min_value} to {max_value}) {length_of_list} times! ').split()))
            if len(values) != length_of_list:
                logger.warning(f'Invalid number of elements! It must contain {length_of_list} values! Try again!')
            elif not all([value in range(min_value, max_value+1) for value in values]):
                logger.warning(f"You entered invalid values: {values}")
            else:
                logger.info(f"You entered valid values: {values}")
                return values
        except ValueError:
            logger.error('ValueError! Only integer is allowed!')

if __name__ == '__main__':
    number_of_shoes = get_valid_number('Enter the available number of shoes (1-9) in the shop: ', 0, 10)
    shoe_sizes = get_a_valid_list(length_of_list=number_of_shoes, min_value=1, max_value=10)
    number_of_customs = get_valid_number('Enter the number of customers in the shop (1-9): ', 0, 10)
    shoes_available = Counter(shoe_sizes)
    total_revenue = 0
    for _ in range(number_of_customs):
        size, price = map(int, input('Preferred size and selling price! ').split())
        if size not in range(1, 11) or price <= 0:
            logger.warning(f"Invalid size or price: size={size}, price={price}. Try again!")
            continue
        if size in shoes_available and shoes_available[size] > 0:
            total_revenue += price
            shoes_available[size] -= 1
    logger.info(f'Total revenue: {total_revenue}')