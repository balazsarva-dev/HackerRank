import numpy as np
from typing import List, Union

def flatten_array(arr: List[Union[int, List[int]]]) -> np.ndarray:
    return np.array(arr, dtype=object).flatten() if arr else np.array([])

if __name__ == '__main__':
    values = [1, 2, [3, 4, 5], 6, [7, 8], 9]
    array_values = flatten_array(values)
    for val in array_values:
        if type(val) == int:
            print(val, end=' ')
        print(val)# Output: [1 2 3 4 5 6 7 8 9]