from itertools import combinations
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def divisibleSumPairs(k: int, ar: list) -> int:
    combination_list = combinations(ar, 2)
    return len(list(filter(lambda x: (x[0] + x[1]) % k == 0, combination_list)))  

def get_valid_input(prompt: str, condition) -> list:
    while True:
        try:
            values = list(map(int, input(prompt).split()))
            if condition(values):
                return values
            else:
                logger.warning("Invalid input. Try again!")
        except ValueError:
            logger.error('Only integer is allowed! Try again! ')

if __name__ == '__main__':
    n, k = get_valid_input('Enter n and k: ', lambda x: len(x) == 2 and x[0] in range(2, 101) and x[1] in range(1, 101))
    valid_list = get_valid_input('Enter n integers: ', lambda x: len(x) == n and all(value in range(1, 101) for value in x))
    logger.info(divisibleSumPairs(k, valid_list))