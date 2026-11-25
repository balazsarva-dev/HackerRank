import sys
from typing import Callable, Tuple, Dict
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def get_valid_number(prompt: str, condition: Callable[[int], bool] | None) -> int:
    while True:
        try:
            n = int(input(prompt))
            if condition is None or condition(n):
                return n
            logger.warning('The input is invalid! Try again! ')
        except ValueError:
            logger.error('You need to input an integer! Try again! ')

def open_a_book(n: int) -> Dict[int, Tuple[int, int]]:
    return {idx : (page, page + 1) for idx, page in enumerate(range(0, n + 1, 2))}

def count_turning_pages(D: Dict[int, Tuple[int, int]], p: int, reverse: bool = False) -> int:
    D = dict(reversed(D.items())) if reverse else D
    return [max(D.keys()) - key for key in D\
            if p in D[key]][0] if reverse\
            else [key for key in D if p in D[key]][0]

def main():
    fptr = sys.stdout
    n = get_valid_number(
                            prompt='Enter the number of pages of your book: ',
                            condition=lambda x: 1 <= x <= 10**5
                        )
    p = get_valid_number(
                            prompt='Enter the page you want to go to: ',
                            condition=lambda x: 1 <= x <= n
                        )
    
    result = open_a_book(n)
    forward = count_turning_pages(result, p)
    backward = count_turning_pages(result, p, reverse=True)
    min_result = min([forward, backward])
    
    final_result = 'You can turn the pages in both directions! ' if forward == backward\
        else 'The shortest way to get there is from the front! ' if forward < backward\
        else 'The shortest way to get there is from the back! '

    fptr.write(final_result+f'You have to turn {min_result} pages.' + '\n')
    fptr.close()
    
if __name__ == '__main__':
    main()