import numpy as np
from typing import Callable

def get_valid_list(expected_length: int, other_condition: Callable) -> list:
    while True:
        try:
            numbers = list(map(int, input().split()))
            if len(numbers) == expected_length and (other_condition is None or other_condition(numbers)):
                return numbers
            print(f'Your list must have {expected_length} values! Try again! ')
        except ValueError:
            print('Invalid value! Try again with integers! ')

def reshape_array(some_list: list) -> np.array:
    return np.reshape(np.array(some_list), (3, 3))

if __name__ == '__main__':
    numbers = get_valid_list(9, lambda x: all(value in range(1, 101) for value in x))
    print(reshape_array(numbers))