import sys

def get_valid_number(condition) -> int:
    while True:
        try:
            n = int(input())
            if condition(n):
                return n
            else:
                print('The input is invalid! Try again! ')
        except ValueError:
            print('You need to input an integer! Try again! ')
        
def open_a_book(n: int) -> dict:
    book = {idx : (page, page + 1) for idx, page in enumerate(range(0, n + 1, 2))}
    book = {k : v for k, v in book.items() if v[0] <= n}
    return book

def counting_steps(D: dict, p: int, straight_or_reversed: str = None) -> list:
    if straight_or_reversed == 'reverse':
        D = dict(reversed(list(D.items())))
        return [max(D.keys()) - key for key in D if p in D[key]][0]
    return [key for key in D if p in D[key]][0]

if __name__ == '__main__':
    fptr = sys.stdout
    n = get_valid_number(lambda x: 1 <= x <= 10**5)
    p = get_valid_number(lambda x: 1 <= x <= n)
    result = open_a_book(n)
    result = [counting_steps(result, p), counting_steps(result, p, 'reverse')]
    result = min(result)
    fptr.write(str(result) + '\n')
    fptr.close()