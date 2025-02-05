def make_one_set(max_length: int) -> set:
    some_set = set()
    while True:
        some_set.update(set(map(int, input().split())))
        if 0 < len(some_set) < max_length:
            return some_set

def get_valid_number(min_value: int, max_value: int) -> int:
    while True:
        try:
            value = int(input())
            if value in range(min_value+1, max_value):
                return value
            print('Out of range! ')
        except ValueError: print('Invalid value! Only integer is allowed! ')

def process(some_set: set, valid_number: int) -> bool:
    counter = 0
    for _ in range(valid_number):
        new_set = make_one_set(max_length=100)
        counter += 1 if some_set.intersection(new_set) == new_set else 0
    return counter == valid_number

def main() -> None:
    set_A, iter_number = make_one_set(max_length=501), get_valid_number(0, 21)
    print(process(set_A, iter_number))

if __name__ == '__main__':
    main()