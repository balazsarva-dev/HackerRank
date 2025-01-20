from collections import Counter
from typing import Optional, Callable

def get_valid_string(prompt: str | None, condition: Optional[Callable[[str], bool]] = None) -> str:
    while True:
        s = input(prompt if prompt is not None else '')
        if condition is None or condition(s):   
            return s
        print("Invalid input. Try again!")

if __name__ == '__main__':
    s = sorted(get_valid_string('', lambda x: len(x) in range(3, 10**4+1) and len(set(x)) >= 3))
    most_common = Counter(s).most_common()[:3]
    for val in most_common:
        print(*val)