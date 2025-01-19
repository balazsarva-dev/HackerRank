from typing import Callable, Union, List, Set

def get_valid_list_or_set(expected_length: int, collection_type: str, condition: Callable) -> List[Union[List[int], Set[int]]]:
    while True:
        try:
            values = list(map(int, input().split()))
            if len(values) == expected_length and (condition is None or condition(values)):
                return values if collection_type == 'list' else set(values)
        except ValueError:
            print('Invalid value! Try again with integers! ')

if __name__ == '__main__':
    n, m = get_valid_list_or_set(2, 'list', lambda x: all(value in range(1, 10**5+1) for value in x))
    common_condition = lambda x: all(value in range(1, 10**9+1) for value in x)
    list_A = get_valid_list_or_set(n, 'list', common_condition)
    set_A, set_B = get_valid_list_or_set(m, 'set', common_condition), get_valid_list_or_set(m, 'set', common_condition)
    print(sum(1 for num in list_A if num in set_A) - sum(1 for num in list_A if num in set_B))