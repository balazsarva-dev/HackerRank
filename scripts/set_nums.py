from typing import Callable, List, Set

def get_valid_list_or_set(prompt: str, length: int, collection_type: str, condition: Callable | None = None) -> List[int] | Set[int]:
    while True:
        try:
            values = list(map(int, input(prompt).split()))
            if len(values) == length and (condition is None or condition(values)):
                if collection_type == 'list':
                    return values
                elif collection_type == 'set':
                    return set(values)
                raise ValueError('Invalid collection type! ')
        except ValueError:
            print('Invalid value! Try again with integers! ')

if __name__ == '__main__':
    n, m = get_valid_list_or_set('Length of 1 list and length of 2 sets: ', 2, 'list', lambda x: all(value in range(1, 10**5+1) for value in x))
    common_condition = lambda x: all(value in range(1, 10**9+1) for value in x)
    list_A = get_valid_list_or_set('Values of the list: ', n, 'list', common_condition)
    set_A = get_valid_list_or_set('Values of the first set: ', m, 'set', common_condition)
    set_B = get_valid_list_or_set('Values of the second set: ', m, 'set', common_condition)
    result = sum(1 for num in list_A if num in set_A) - sum(1 for num in list_A if num in set_B)
    print(result)