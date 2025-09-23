from numpy import typing, array, dot, array_str
from typing import Callable
import logging 

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def get_valid_number(prompt: str, condition: Callable = None) -> int:
    while True:
        try:
            N = int(input(prompt))
            if condition is None or condition(N):
                return N
            else:
                logger.warning('The input is invalid! Try again! ')
        except ValueError:
            logger.error('You need to input an integer! Try again! ')

def make_a_square_matrix(prompt: str) -> typing.NDArray:
    number_of_rows = get_valid_number(prompt, lambda x: x in range(1, 6))
    matrix = []    
    for _ in range(number_of_rows):
        while True:
            try:
                row = list(map(int, input('Enter the values of the row: ').split()))
                if len(row) == number_of_rows:
                    matrix.append(row)
                    break
                logger.warning(f'You need to input {number_of_rows} integers! Try again! ')
            except ValueError:
                logger.error('You need to input integers! Try again! ')
    return array(matrix)

def main():
    logger.info('Matrix Multiplication Program')
    A = make_a_square_matrix('Enter the number of rows and columns of one square matrix: ')
    while True:
        B = make_a_square_matrix('Enter the number of rows and columns of another square matrix: ')
        if A.shape[1] == B.shape[0]:
            logger.info(f'Matrix A: \n{array_str(A)}\n')
            logger.info(f'Matrix B: \n{array_str(B)}\n')
            return dot(A, B)
        else: logger.warning('The number of columns of matrix A must be equal to the number of rows of matrix B! Try again! ')

if __name__ == '__main__':
    result = main()
    if result is not None:
        logger.info(f'Product of the matrices is:\n{array_str(result)}')