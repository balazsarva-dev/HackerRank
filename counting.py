import re
import time
import logging
from typing import Any

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def is_valid_name(name: str) -> bool:
    return bool(re.match(r'^[a-zA-Z]{4,15}$', name))

def enter_name() -> str:
    while True:
        name = input('What is your name? ')
        if is_valid_name(name):
            return name.title()
        logger.warning('Invalid name! Your name must be between 4 and 15 alphabetic characters!')

def countdown(seconds: int, feature: str, feature_value: Any) -> None:
    logger.info(f'Your {feature} appears in')
    while seconds > 0:
        logger.info(f'{seconds}...')
        seconds -= 1
        time.sleep(1)
    logger.info(f'Time is up! Your {feature} is: {feature_value} ')

def main() -> None:
    enter_your_name = enter_name()
    countdown(seconds=5, feature='name', feature_value=enter_your_name)
    logger.info('Goodbye! ')

if __name__ == '__main__':
    main()