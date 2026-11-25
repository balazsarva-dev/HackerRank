import re
import time
import logging
from typing import Any

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def is_valid_name(name: str) -> bool:
    """
    Validates if the given name is between 4 and 15 alphabetic characters.

    :param name: The name to validate.
    :return: True if the name is valid, False otherwise.
    """
    return bool(re.match(r'^[a-zA-ZáéíóöőúüűÁÉÍÓÖŐÚÜŰ]{4,15}$', name))

def enter_name() -> str:
    """
    Prompts the user to enter a valid name.

    :return: The validated name in title case.
    """
    while True:
        name = input('What is your name? ')
        if is_valid_name(name):
            return name.title()
        logger.warning('Invalid name! Your name must be between 4 and 15 alphabetic characters!')

def countdown(seconds: int, feature: str, feature_value: Any) -> None:
    """
    Performs a countdown and displays the feature value at the end.

    :param seconds: The number of seconds to count down.
    :param feature: The name of the feature being displayed.
    :param feature_value: The value of the feature to display.
    """
    try:
        logger.info(f'Your {feature} appears in')
        while seconds > 0:
            logger.info(f'{seconds}...')
            seconds -= 1
            time.sleep(1)
        logger.info(f'Time is up! Your {feature} is: {feature_value} ')
    except KeyboardInterrupt:
        logger.warning('Countdown interrupted by user!')

def main() -> None:
    """
    Main function to execute the program logic.
    """
    enter_your_name = enter_name()
    countdown_seconds = 5
    countdown(seconds=countdown_seconds, feature='name', feature_value=enter_your_name)
    logger.info('Goodbye! ')

if __name__ == '__main__':
    main()