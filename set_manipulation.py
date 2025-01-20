from typing import Dict, Set, Callable

def make_a_set(expected_length: int) -> Set[int]:
    some_set: Set[int] = set()
    while len(some_set) != expected_length:
        try:
            values = set(map(int, input(f'Enter {expected_length} integers: ').split()))
            if len(values) == expected_length:
                some_set.update(values)
            print(f'Invalid number of values, try again! It should be {expected_length}!')
        except ValueError:
            print('Invalid value, try again!')
    return some_set

def take_actions(some_set: Set[int]) -> Dict[str, Callable]:
    return {
        'intersection_update': some_set.intersection_update,
        'update': some_set.update,
        'symmetric_difference_update': some_set.symmetric_difference_update,
        'difference_update': some_set.difference_update
        }

def get_valid_number(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_value < value < max_value:
                return value
            print(f'Invalid value, try again from range {min_value}-{max_value}!')
        except ValueError:
            print('Invalid value (only integer is allowed), try again!')

if __name__ == '__main__':
    number_of_elements = get_valid_number('Enter the number of elements in the set: ', 1, 12)
    make_set_A = make_a_set(number_of_elements)
    actions = take_actions(make_set_A)
    options = actions.keys()

    N = get_valid_number('Enter the number of commands: ', 1, 6)
    for _ in range(N):
        while True:
            command_input = input(f'Enter a command from {list(options)} and the length of the new set: ').split()
            command = command_input[0]
            if len(command_input) != 2 or command not in options:
                print('Invalid command! Try again!')
                continue
            command = command_input[0]
            try:
                values = set(map(int, input().split()))
                if len(values) != int(command_input[1]):
                    print('Invalid number of values! Try again!')
                    continue
                actions[command](values)
                break
            except ValueError:
                print('Invalid value, only integer is allowed! Try again!')      
    print(sum(make_set_A))