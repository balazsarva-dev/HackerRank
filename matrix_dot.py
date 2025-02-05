from numpy import typing, array, dot
from typing import Callable

def get_valid_number(prompt: str, condition: Callable) -> int:
    while True:
        try:
            N = int(input(prompt))
            if condition(N):
                return N
            else:
                print('The input is invalid! Try again! ')
        except ValueError:
            print('You need to input an integer! Try again! ')

def make_a_square_matrix(prompt: str) -> typing.NDArray:
    N = get_valid_number(prompt, lambda x: x in range(1, 6))
    my_2D_list = []    
    for _ in range(N):
        while True:
            try:
                row = list(map(int, input('Enter the values of the row: ').split()))
                if len(row) == N:
                    my_2D_list.append(row)
                    break
                print(f'You need to input {N} integers! Try again! ')
            except ValueError:
                print('You need to input integers! Try again! ')
    return array(my_2D_list)

def main():
    A = make_a_square_matrix('Enter the number of rows and columns of one square matrix: ')
    while True:
        B = make_a_square_matrix('Enter the number of rows and columns of another square matrix: ')
        if A.shape[1] == B.shape[0]:
            print(f'Matrix A: \n{A}\n')
            print(f'Matrix B: \n{B}\n')
            return dot(A, B)
        else: print('The number of columns of matrix A must be equal to the number of rows of matrix B! Try again! ')

if __name__ == '__main__':
    print(f'Product of the matrices is:\n{main()}')