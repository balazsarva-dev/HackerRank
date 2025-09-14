from typing import List, Callable
from numpy import typing as np_typing
import numpy as np
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def get_valid_list(condition: Callable | None) -> List[int]:
    while True:
        try:
            values = list(map(int, input().split()))
            if condition is None or condition(values):
                return values
            logging.warning('Conditions are not valid! Try again! ')
        except ValueError:
            logging.error('Only integer is allowed! Try again! ')

def make_array(number_of_row: int, number_of_columns: int) -> np_typing.NDArray[np.int_]:
    two_d_array = []
    for _ in range(number_of_row):
        while True:
            try:
                values = list(map(int, input().split()))
                if len(values) == number_of_columns:
                    two_d_array.append(values)
                    break            
            except ValueError:
                logging.error('Only integer is allowed! Try again! ')
    return np.array(two_d_array)

def main() -> None:
    n, m, p = get_valid_list(lambda x: len(x) == 3 and all(v in range(20) for v in x))
    first_array = make_array(n, p) 
    second_array = make_array(m, p)
    logger.info(np.concatenate((first_array, second_array)))

if __name__ == '__main__':
    main()
