import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

# Function to count how many fruits fall within the house range inclusive the tree position
def countApplesAndOranges(s: int, t: int, tree_position: int, fruits: list[int]) -> int:
    '''Counting how many fruits fall within the house range inclusive the tree position'''
    return sum(1 for location in fruits if tree_position + location in range(s, t+1))

# Function to get VALID inputs from the user
def get_inputs(prompt: str, expected_length: int) -> list[int]:
    '''Requires inputs from the user and ensures they are valid'''
    while True:
        try:
            values = input(prompt).split()
            if len(values) != expected_length:
                logger.warning(f'Invalid number of elements! It must contain {expected_length} values! Try again! ')
                continue
            return list(map(int, values))
        except ValueError:
            logger.error('Invalid input! Every value must be integer! Try again! ')

# Main function - it requires inputs from the user, in this case 
# the house positions, tree positions, and fruit distances.
def main() -> None:
    s, t = get_inputs('Enter s and t: ', 2)
    a, b = get_inputs('Enter a and b: ', 2)
    m, n = get_inputs('Enter m and n: ', 2)

    apples = get_inputs('Enter the positions of the apples: ', m)
    oranges = get_inputs('Enter the positions of the oranges: ', n)

    result = countApplesAndOranges(s, t, a, apples), countApplesAndOranges(s, t, b, oranges)
    logger.info(f'Apples: {result[0]}, Oranges: {result[1]}')

if __name__ == '__main__':
    main()
