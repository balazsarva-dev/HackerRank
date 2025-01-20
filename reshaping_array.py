import numpy as np
from typing import Callable, List

def get_valid_list(prompt: str, expected_length: int, other_condition: Callable | None = None) -> List[int]:
    while True:
        try:
            numbers = list(map(int, input(prompt).split()))
            if len(numbers) == expected_length and (other_condition is None or other_condition(numbers)): return numbers
            print(f'Your list must have {expected_length} values! Try again! ')
        except ValueError: print('Invalid value! Try again with integers! ')

def reshape_array_with_specified_rows_and_columns(some_list: List[int]) -> np.ndarray:
    while True:
        try:
            rows = int(input('Enter the number of rows: '))
            if len(some_list) % rows != 0:
                print('The number of rows must be a factor of the total number of values! Try again! ')
                continue
            columns = len(some_list) // rows
            return np.reshape(np.array(some_list), (rows, columns))
        except ValueError: print('You need to input an integer! Try again! ')
        except ZeroDivisionError: print('You cannot have zero rows! Try again! ')

if __name__ == '__main__':
    number = get_valid_list('Enter the expected length of the array: ', 1, lambda x: len(x) == 1 and x[0] in range(1, 10))
    numbers = get_valid_list('Enter the values of the array: ', number[0], lambda x: all(value in range(1, 101) for value in x))
    print(reshape_array_with_specified_rows_and_columns(numbers))
