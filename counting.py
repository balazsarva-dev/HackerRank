import time
import logging
from typing import Any

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def enter_name() -> str:
    while True:
        name = input('What is your name? ')
        if not name:
            logger.warning('Please enter a valid name! ')
        elif not name.isalpha():
            logger.error('Only alphabetic character is valid! ')
        elif len(name) not in range(4, 16):
            logger.warning('Name must be between 4 and 15 characters! ')
        else:
            return name.title()

def countdown(seconds: int, feature : str, feature_value : Any) -> None:
    print(f'Your {feature} appear in')
    while seconds > 0:
        logger.info(f'{seconds}...')
        seconds -= 1
        time.sleep(1)
    logger.info(f'Time is up! Your {feature} is: {feature_value} ')

def main() -> None:
    enter_your_name = enter_name()
    countdown(seconds=5, feature='name', feature_value=enter_your_name)
    logger.debug('Goodbye! ')

if __name__ == '__main__':
    main()