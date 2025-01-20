from typing import List, Callable
from numpy import typing as np_typing
import numpy as np

def get_valid_list(condition: Callable | None) -> List[int]:
    while True:
        try:
            values = list(map(int, input().split()))
            if condition is None:
                return values
            if condition(values):
                return values
            print('Conditions are not valid! Try again! ')
        except ValueError:
            print('Only integer is allowed! Try again! ')

def make_array(number_of_row: int, number_of_columns: int) -> np_typing.NDArray:
    ndarray = []
    for _ in range(number_of_row):
        while True:
            try:
                values = list(map(int, input().split()))
                if len(values) == number_of_columns:
                    ndarray.append(values)
                    break            
            except ValueError:
                print('Only integer is allowed! Try again! ')
    return np.array(ndarray)
    
if __name__ == '__main__':
    n, m, p = get_valid_list(lambda x: len(x) == 3 and all(v in range(20) for v in x))
    first_array = make_array(n, p) 
    second_array = make_array(m, p)
    print(np.concatenate((first_array, second_array)))
        
    