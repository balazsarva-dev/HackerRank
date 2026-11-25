from collections import deque
from typing import Deque

def get_valid_number(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value in range(min_value, max_value+1):
                return value
            else:
                print(f'Invalid range! Value must be between {min_value}-{max_value} Try again! ')
        except ValueError:
            print('Invalid value! Try again with integer! ')

def make_a_deque(expected_length: int = 1) -> Deque[int]:
    while True:
        try:
            values = list(map(int, input().split()))
            if len(values) == expected_length:
                return deque(values)
            else:
                print(f'Invalid number of values! It must contain {expected_length} values! Try again! ')
        except ValueError:
            print('Invalid input. Please enter integers only.')

def pop_left_right(some_deque: Deque[int]) -> Deque[int]:
    empty = deque()
    while some_deque:
        empty.append(some_deque.pop() if some_deque[0] <= some_deque[-1] else some_deque.popleft())
    return empty
    
if __name__ == '__main__':
    T = get_valid_number('Enter a valid iteration number from 1 to 5: ', 1, 5)
    for _ in range(T):
        number_of_cubes = get_valid_number('Enter the number of cubes: ', 1, 10**5)
        some_deque = make_a_deque(number_of_cubes)
        max_value, min_value = max(some_deque), min(some_deque)
        result = pop_left_right(some_deque)
        condition = all([result[0] == max_value, result[-1] == min_value])
        print('Yes' if condition else 'No')