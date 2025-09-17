from collections import deque
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def get_valid_number(prompt: str, min_value: int, max_value: int) -> int:
    """Get a valid number from user input within a specified range.

    Args:
        prompt (str): The prompt message to display to the user.
        min_value (int): The minimum valid value (exclusive).
        max_value (int): The maximum valid value (exclusive).

    Returns:
        int: The valid number entered by the user.
    """
    while True:
        try: 
            value = int(input(prompt))
            if min_value <= value < max_value:
                logger.info(f'Valid value received: {value}')
                return value
            else:
                logger.warning('Invalid range! Try again! ')
        except ValueError:
            logger.error('Invalid value! Only integer is allowed! ')

def get_valid_string(prompt: str, *args: str) -> str:
    """
    Get a valid string from user input that matches one of the specified arguments.
    """
    while True:
        input_value = input(prompt)
        if input_value in args:
            logger.info(f'Valid string received: {input_value}')
            return input_value
        logger.warning('Invalid string! Try again! ')

def make_actions(some_deque: deque) -> dict:
    """
    Returns a dictionary of deque operations.
    """
    return {
        'append':some_deque.append,
        'appendleft':some_deque.appendleft,
        'pop':some_deque.pop,
        'popleft':some_deque.popleft
    }
    
def main():
    N = get_valid_number('Enter the number of commands between 1 and 15: ', 1, 16)
    d: deque[int] = deque()
    actions = make_actions(d)
    for _ in range(N):
        while True:
            try:
                command_input = get_valid_string(f"Enter a command from {list(actions.keys())}: ", *actions.keys())
                if command_input in ['pop', 'popleft']:
                    if not d:
                        logger.warning(f"Cannot perform '{command_input}' on an empty deque!")
                        break
                    actions[command_input]()
                else:
                    args = map(int, input('Enter arguments (if any): ').split())
                    actions[command_input](*args)
                    break
            except ValueError:
                logger.error('Invalid input! Only integer is allowed! Try again! ')
            except TypeError:
                logger.error('Invalid arguments! Try again! ')
    logger.info(f'Result: {d}')
    return d

if __name__ == '__main__':
    main()