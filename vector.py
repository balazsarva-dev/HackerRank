from numpy import typing, array, inner, outer
import logging

logger = logging.getLogger(__name__)    
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def get_valid_size(min_value: int = 1, max_value: int = 10) -> int:
    while True:
            try:
                size = int(input(f'Enter the size of the vectors from {min_value} to {max_value}: '))
                if size in range(min_value, max_value+1):
                    return size
                logger.error(f'Invalid size! It must be between {min_value}-{max_value}! Try again! ')
            except ValueError:
                logger.error('Invalid input! Please enter an integer!')
                
def make_a_vector(size: int=2) -> typing.NDArray:
    while True:
        try:
            values = list(map(int, input(f'Enter {size} integers separated by space: ').split()))
            if len(values) == size:
                logger.info(f'Vector created {values}')
                return array(values)
            else:
                logger.error('Invalid number of values! It must contain %s values! Try again! ', size)
        except ValueError:
            logger.error('Invalid input! Please enter integers only! ')

def calculate_produts(A: typing.NDArray, B: typing.NDArray, inner_operation: bool | None = True) -> typing.NDArray:
    return inner(A, B) if inner_operation else outer(A, B)

if __name__ == '__main__':
    test_size = get_valid_size()
    A = make_a_vector(size=test_size)
    B = make_a_vector(size=test_size)
    inner_product, outer_product = calculate_produts(A, B), calculate_produts(A, B, inner_operation=False)
    logger.info(f'Inner product: {inner_product}')
    logger.info(f'Outer product: {outer_product}')