from itertools import product
import logging 

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def make_a_list(length: int, min_val: int, max_val: int) -> list:
    while True:
        values = input(f'Setup a list! Length must be {length}! Values between: {min_val}-{max_val}: ').split()
        try:
            int_values = list(map(int, values))
            if len(int_values) != length:
                logger.warning('Invalid length! Try again! ')
            elif all(value in range(min_val, max_val+1) for value in int_values):
                return int_values
            else:
                logger.warning('You value(s) is/are out of range! ')
        except ValueError:
            logger.error('Only integer is allowed! ')

def getMoneySpent(keyboards: list[int], drives: list[int], budget: int) -> int:
    return max((s for s in (sum(pair) for pair in product(keyboards, drives)) if s <= budget), default=-1)

def setup_bnm() -> list[int]:
    while True:
        values = input('Setup budget, and the number of keyboards and drives: ').split()
        try:
            bnm = list(map(int, values))
            if len(bnm) != 3:
                logger.warning('Your list is invalid! It must have 3 values! ')
            elif bnm[0] not in range(1, 10**6+1) or bnm[1] not in range(1, 1001) or bnm[2] not in range(1, 1001):
                logger.warning('Your values are out of range! Try again! ')
            else:
                return bnm
        except ValueError:
            logger.error('Only integer is allowed! Try again!') 

def main():
    bnm = setup_bnm()
    keyboards = make_a_list(bnm[1], 1, 10**6)
    drives = make_a_list(bnm[2], 1, 10**6)
    moneySpent = getMoneySpent(keyboards, drives, bnm[0])
    logger.info(f'Maximum amount of money she can spend: {moneySpent}')

def test_run():
    keyboards = [40, 50, 60]
    drives = [5, 8, 12]
    budget = 60
    result = getMoneySpent(keyboards, drives, budget)
    assert result == 58, f"Expected 58, but got {result}"
    logger.info(f'Test result: {result}')

if __name__ == '__main__':
    test_run()
    logger.info("All tests passed!")
    main()