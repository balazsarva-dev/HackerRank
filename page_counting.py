import sys
from typing import Callable, Optional, Tuple, Dict, List

def get_valid_number(condition: Optional[Callable[[int], bool]]) -> int:
    while True:
        try:
            n = int(input())
            if condition(n):
                return n
            print('The input is invalid! Try again! ')
        except ValueError:
            print('You need to input an integer! Try again! ')
        
def open_a_book(n: int) -> Dict[int, Tuple[int, int]]:
    return {idx : (page, page + 1) for idx, page in enumerate(range(0, n + 1, 2))}

def count_turning_pages(D: Dict[int, Tuple[int, int]], p: int, reverse : Optional[bool] = False) -> int:
    if reverse:
        D = dict(reversed(list(D.items())))
        return [max(D.keys()) - key for key in D if p in D[key]][0]
    return [key for key in D if p in D[key]][0]

if __name__ == '__main__':
    fptr = sys.stdout
    n = get_valid_number(lambda x: 1 <= x <= 10**5)
    p = get_valid_number(lambda x: 1 <= x <= n)
    result = open_a_book(n)
    result = [count_turning_pages(result, p), count_turning_pages(result, p, reverse=True)]
    result = min(result)
    fptr.write(str(result) + '\n')
    fptr.close()