from collections import deque
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def get_valid_number(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        try: 
            value = int(input(prompt))
            if min_value < value < max_value:
                logger.info(f'Valid value received: {value}')
                return value
            else:
                logger.warning('Invalid range! Try again! ')
        except ValueError:
            logger.error('Invalid value! Only integer is allowed! ')

def get_valid_string(prompt: str, *args: str) -> str:
    while True:
        input_value = input(prompt)
        if input_value in args:
            logger.info(f'Valid string received: {input_value}')
            return input_value
        logger.warning('Invalid string! Try again! ')

def make_actions(some_deque: deque) -> dict:
    return {
        'append':some_deque.append,
        'appendleft':some_deque.appendleft,
        'pop':some_deque.pop,
        'popleft':some_deque.popleft
    }
    
def main():
    N = get_valid_number('Enter the number of commands between 1 and 100: ', 1, 101)
    d: deque[int] = deque()
    actions = make_actions(d)
    for _ in range(N):
        command_input = get_valid_string(f"Enter a command from {list(actions.keys())}: ", *actions.keys())
        while True:
            try:
                args = map(int, input('Enter arguments (if any): ').split())
                break
            except ValueError:
                logger.error('Invalid input! Only integer is allowed! Try again! ')
        try:
            actions[command_input](*args)
        except TypeError:
            logger.error('Invalid arguments! Try again! ')
    logger.info(f'Result: {d}')
    return d

if __name__ == '__main__':
    main()

    # N = get_valid_number('Enter the number of commands between 1 and 100: ', 1, 101)
    # d: deque[int] = deque()
    # actions = make_actions(d)
    # for _ in range(N):
    #     while True:
    #         command_input = input().split()
    #         command = command_input[0]
    #         try:
    #             args = map(int, command_input[1:])
    #         except ValueError:
    #             print('Only integer is allowed! Try again! ')
    #         if command in actions.keys():
    #             try:
    #                 actions[command](*args)
    #                 break
    #             except TypeError:
    #                 print('Invalid argument! Try again! ')
    #         print('Invalid command! Try again!')
    # print(*d)