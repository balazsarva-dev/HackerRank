# def sort_odd_before_even(somelist: list) -> tuple[list, list]:
#     result, odd_numbers, even_numbers = [], [], []
#     for value in somelist:
#         try: 
#             value = int(value)
#             if value % 2 == 0: even_numbers.append(str(value))
#             else: odd_numbers.append(str(value))
#         except ValueError: result.append(value)
#     odd_numbers.sort()
#     even_numbers.sort()
#     odd_numbers.extend(even_numbers)
#     result.extend(odd_numbers)
#     return result

# if __name__ == '__main__':
#     S = input()
#     list_string = list(S)
#     list_string.sort()
#     list_string.sort(key=str.isupper)
#     list_string.sort(key=str.isdigit)
#     print(''.join(sort_odd_before_even(list_string)))

# from typing import Callable, Optional

# def get_valid_input(prompt: str, condition: Optional[Callable[[str], bool]] = None) -> str:
#     while True:
#         values = input(prompt)
#         if not values: return 'Sorting1234'
#         if condition is None or condition(values): return values
#         print('Invalid input. Try again! ')

# def sorting_strings(some_string: str) -> str:
#     list_string = list(some_string)   
#     list_string.sort(key=lambda x: (x.isdigit(), x.isupper(), x.islower(), x))
#     numbers = []
#     for char in list_string:
#         if char.isdigit(): 
#             list_string.remove(char)
#             numbers.append(char)
#     odds, evens = [], []
#     for number in numbers:
#         if int(number) % 2 == 1:
#             odds.append(number)        
#     return ''.join(list_string + odds)

# if __name__ == '__main__':
#     S = get_valid_input('Enter a string: ', lambda x: len(x) in range(1, 1000))
#     print(sorting_strings(S))

from typing import Callable, Optional

def get_valid_input(prompt: str, condition: Optional[Callable[[str], bool]] = None) -> str:
    while True:
        values = input(prompt)
        if not values: return 'Sorting1234'
        if condition is None or condition(values): return values
        print('Invalid input. Try again! ')

def sorting_strings(some_string: str) -> str:
    letters, odds, evens = [], [], []
    for char in some_string:
        letters.append(char) if char.isalpha() else odds.append(char) if int(char) % 2 == 1 else evens.append(char)
    letters.sort(key=lambda x: (x.isupper(), x.islower(), x))
    return ''.join(letters+odds+evens)
    
if __name__ == '__main__':
    S = get_valid_input('Enter a string: ', lambda x: len(x) in range(1, 1000))
    print(sorting_strings(S))