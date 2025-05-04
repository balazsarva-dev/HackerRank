from typing import Callable, Optional

def get_valid_input(prompt: str, condition: Optional[Callable[[str], bool]] = None) -> str:
    while True:
        values = input(prompt)
        if not values: return 'Sorting1234'
        if condition is None or condition(values): return values
        print('Invalid input. Try again! ')

def sorting_strings(some_string: str) -> str:
    letters, odds, evens, not_relevant = [], [], [], []
    for char in some_string:
        try:
            letters.append(char) if char.isalpha()\
            else odds.append(char) if int(char) % 2 == 1\
            else evens.append(char)
        except ValueError:
            not_relevant.append(char)
    letters.sort(key=lambda x: (x.isupper(), x.islower(), x))
    return ''.join(letters+odds+evens+not_relevant)
    
if __name__ == '__main__':
    S = get_valid_input('Enter a string: ', lambda x: len(x) in range(1, 1000))
    print(sorting_strings(S))