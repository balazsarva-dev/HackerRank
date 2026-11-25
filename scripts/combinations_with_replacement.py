from itertools import combinations_with_replacement 
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


def get_valid_int_input(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            logger.warning(f'Range warning! Enter a number between {min_value} and {max_value}! ')
        except ValueError:
            logger.warning('Invalid input! Please enter a valid integer.')
            continue

def generate_combinations_with_replacement(characters: str, k: int) -> None:
    result = combinations_with_replacement(sorted(characters), k)
    for combination in result:
        logger.info(''.join(combination))

def main() -> None:
    S = input('Enter the string: ').upper()
    k = get_valid_int_input(f'Enter the size of combinations (1 to {len(S)}): ', 1, len(S))
    generate_combinations_with_replacement(S, k)

if __name__ == '__main__':
    main()