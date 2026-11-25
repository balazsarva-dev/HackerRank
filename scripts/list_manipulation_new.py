import sys
import logging
from typing import Callable, List, Dict, Any

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('config.log')
console_formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
file_formatter = console_formatter
stream_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

def take_actions(L: List[Any]) -> Dict[str, Callable]:
    return {'print': lambda: logger.info(L),
            'remove': L.remove,
            'append': L.append,
            'sort': L.sort,
            'pop': L.pop,
            'reverse': L.reverse,
            'insert': L.insert}

def get_valid_number(min_value: int = 1, max_value: int = 10) -> int:
    while True:
        try:
            N = int(input(f'Set a value from {min_value} to {max_value}! '))
            if N in range(min_value, max_value+1):
                logger.info(f'Well done! Your chosen value is {N}. ')
                return N
            else:
                logger.warning(f'Out of range! Value must be between {min_value} and {max_value}. Try again!')
        except ValueError:
            logger.error('Only integer is allowed! Try again! ')

def calling_actions(number_of_actions: int) -> List[Any]:
    L: List[Any] = []
    actions = take_actions(L)
    for _ in range(number_of_actions):
        while True:
            command_input = input(f'Enter your command and the arguments {list(actions.keys())} separated by space! ').split()
            if not command_input or len(command_input) > 3:
                logger.error('Invalid input! Please enter a command and up to three arguments.')
                continue
            command = command_input[0]
            if command not in actions:
                logger.error(f'Invalid command! Available commands are: {list(actions.keys())}. Try again!')
                continue
            try:
                args = map(int, command_input[1:])
                logger.info(f'Command #{_} executed: {command} with arguments {command_input[1:]}.')
                actions[command](*args)
                break
            except ValueError:
                logger.error('Only integer is allowed regarded arguments! Try again! ')
            except TypeError:
                logger.error('Missing, or invalid number of arguments! Try again! ')
    logger.info(f'Final list: {L}')
    return L

def main():
    logger.info('Starting the program...')
    number_of_commands = get_valid_number()
    return calling_actions(number_of_commands)

if __name__ == '__main__':
    main()