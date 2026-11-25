def get_valid_number(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_value < value < max_value:
                return value
            else:
                print(f'Out of range! Try again from range {min_value}-{max_value}!')
        except ValueError:
            print(f'Invalid value, try again from range {min_value}-{max_value}!')

def make_a_set(prompt: str, length: int) -> set:
    some_set = set()
    while len(some_set) != length:
        some_set.update(set(map(int, input(prompt).split())))
        if len(some_set) not in range(1, length + 1):
            print(f'Out of range! The set must contain {length} DIFFERENT elements!')
            continue
    return some_set
    
if __name__ == '__main__':
    T = get_valid_number('Enter a valid number from 0 to 21: ', 0, 21)
    for _ in range(T):
        length_A = get_valid_number('Enter a valid number from 0 to 1000: ', 0, 1001)
        set_A = make_a_set(prompt="Enter the elements in the set: ", length=length_A)
        length_B = get_valid_number('Enter a valid number from 0 to 1000: ', 0, 1001)
        set_B = make_a_set(prompt="Enter the elements in the set: ", length=length_B)
        print(set_A.intersection(set_B) == set_A)