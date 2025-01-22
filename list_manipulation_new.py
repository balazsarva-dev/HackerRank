import sys
import logging
from typing import Callable, List, Dict, Any

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)

def take_actions(L: List[Any]) -> Dict[str, Callable]:
    return {'print': lambda: print(L),
            'remove': L.remove,
            'append': L.append,
            'sort': L.sort,
            'pop': L.pop,
            'reverse': L.reverse,
            'insert': L.insert}

def set_commands(min_value: int = 1, max_value: int = 10) -> int:
    while True:
        try:
            N = int(input(f'Set a value from {min_value} to {max_value}! '))
            if N in range(min_value, max_value+1):
                logger.info(f'Well done! Your chosen value is {N}. ')
                return N
            else:
                logger.error(f'Out of range! Value must be between {min_value} and {max_value}. Try again!')
        except ValueError:
            logger.critical('Only integer is allowed! Try again! ')

def calling_actions(number_of_actions: int):
    L: List[Any] = []
    actions = take_actions(L)
    for _ in range(number_of_actions):
        while True:
            command_input = input('Enter your command and the arguments separated by space! ').split()
            command = command_input[0]
            try:
                args = map(int, command_input[1:])
                if command in actions:
                    actions[command](*args)
                    break
                else:
                    logger.error(f'Invalid command! You must choose from {actions.keys()}! Try again! ')
            except ValueError:
                logger.critical('Only integer is allowed! Try again! ')
            except TypeError:
                logger.critical('Invalid number of arguments! Try again! ')
    return L
def main():
    N = set_commands()
    return calling_actions(N)

if __name__ == '__main__':
    print(main())