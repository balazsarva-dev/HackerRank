import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def catAndMouse(x: int, y: int, z: int) -> str:
    cat_b = 'Cat B', abs(z - y)
    cat_a = 'Cat A', abs(z - x)
    mouse_c = 'Mouse C'
    result = cat_b[0] if cat_b[1] < cat_a[1] else mouse_c if cat_b[1] == cat_a[1] else cat_a[0]
    return result

def get_number_of_queries(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        try:
            q = int(input(prompt))
            if not min_value <= q <= max_value:
                logger.error(f'The number of queries must be in the range [{min_value}, {max_value}]! Please try again! ')
                continue
            return q
        except ValueError:
            logger.error('Invalid value! The number of queries must be an integer! ')
            continue

def main():
    q = get_number_of_queries('Enter the number of queries: ', 1, 100)
    for _ in range(q):
        x, y, z = map(int, input('Enter the position of Cat A, Cat B and the Mouse: ').split())
        result = catAndMouse(x, y, z)
        logger.info(f'Result: {result}')

if __name__ == '__main__':
    main()