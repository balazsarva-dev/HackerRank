import numpy as np
from typing import Callable

def get_valid_list(expected_length: int, other_condition: Callable) -> list:
    while True:
        try:
            numbers = list(map(int, input('Enter the values of the array! ').split()))
            if len(numbers) == expected_length and (other_condition is None or other_condition(numbers)):
                return numbers
            print(f'Your list must have {expected_length} values! Try again! ')
        except ValueError:
            print('Invalid value! Try again with integers! ')

def reshape_array_with_specified_rows_and_columns(some_list: list) -> np.array:
    while True:
        try:
            rows = int(input('Enter the number of rows: '))
            if len(some_list) % rows != 0:
                print('The number of rows must be a factor of the total number of values! Try again! ')
                continue
            columns = len(some_list) // rows
            break
        except ValueError:
            print('You need to input an integer! Try again! ')
        except ZeroDivisionError:
            print('You cannot have zero rows! Try again! ')
    return np.reshape(np.array(some_list), (rows, columns))

# def reshape_array(some_list: list) -> np.array:
#     return np.reshape(np.array(some_list), (3, 3))

if __name__ == '__main__':
    while True:
        try:
            number_of_elements = int(input('Enter the number of elements: '))
            if number_of_elements in range(1, 101):
                break
            else:
                print('The number of elements must be between 1 and 100! Try again! ')
        except ValueError:  
            print('You need to input an integer! Try again! ')
            
    numbers = get_valid_list(number_of_elements, lambda x: all(value in range(1, 101) for value in x))
    print(reshape_array_with_specified_rows_and_columns(numbers))
    # print(reshape_array(numbers))