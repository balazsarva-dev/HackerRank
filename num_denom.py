from fractions import Fraction
from functools import reduce
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def product(fracs: list[Fraction]) -> tuple[int, int]:
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

def get_fraction_input() -> Fraction:
    while True:
        try:
            inputs = list(input('Enter the numerator and the denominator (e.g., "1 2"): ').split())
            if len(inputs) != 2:
                logger.warning('You need to input exactly two integers! Try again!')
                continue
            numerator, denominator = map(int, inputs)
            if denominator == 0:
                logger.warning('Denominator cannot be zero! Try again!')
                continue
            return Fraction(numerator, denominator)
        except ValueError:
            logger.error('Only integers are allowed! Try again!')


def get_valid_int(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                logger.warning(f'Please enter an integer between {min_value} and {max_value}.')
        except ValueError:
            logger.error('Invalid input! Please enter an integer.')

def main():
    num_of_fractions = get_valid_int('Enter the number of fractions: ', 1, 100)
    fracs = []
    for _ in range(num_of_fractions):
        fracs.append(get_fraction_input())
    result = product(fracs)
    logger.info('The product of the fractions')
    logger.info(f'Fractions: {", ".join(map(str, fracs))}')
    logger.info(f'Product: {result[0]}/{result[1]}')

if __name__ == '__main__':
    main()