import logging
import sys
from typing import Generator

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

FILENAME = 'guest_list.txt'

def read_guests_from_file(file_name: str) -> Generator[str, None, None]:
    if not file_name:
        logger.error('File name is missing! ')
        return

    try:
        with open(file_name, 'r') as file:
            for line in file:
                if line := line.strip(): 
                    yield line

    except FileNotFoundError:
        logger.error('File not found! ')
    except IOError:
        logger.error(f'Error reading from {file_name}! ')
        
def add_data_to_a_file(file_name: str, data: str) -> bool:
    if not file_name or not data:
        logger.error('File name or data is missing! ')
        return False
    
    try:
        with open(file_name, 'a') as file:
            file.write(f'{data}\n')
            file.flush()
        return True

    except IOError as e:
        logger.error(f'Error writing to {file_name}: {e}! ')
        return False
        
def display_guests(file_name: str) -> None:
    logger.info('\nGuest list: \n')
    guests = read_guests_from_file(file_name)
    for guest in guests:
        logger.info(guest)

def validate_guest():
    while True:
        guest_input = yield
        if not guest_input or len(guest_input.split()) != 2:
            yield None, 'Please enter guest name and age! '

        try:
            name, age = guest_input.split()
            if not name.isalpha():
                yield 'Name must be alphabetic! '

            age = int(age)
            if age not in range(18, 101):
                yield None, 'Guest must be between 18 and 100 years old! '

            yield f'{name},{age}', None

        except ValueError:
            yield None, 'Age must be number! '

def add_guest(prompt: str) -> None:
    guest_validator = validate_guest()
    next(guest_validator)
    
    while True:
        try:
            new_guest = input(prompt)
            result = guest_validator.send(new_guest)
            data, error = result
            if data and ',' in data:
                if added_data := add_data_to_a_file(FILENAME, data):
                    logger.info('Guest added successfully!')
                    return
                else:
                    logger.error('Failed to add guest to file!')
            elif error:
                logger.error(result)
            else:
                logger.error('Invalid input! Try again!')
                
        except KeyboardInterrupt:
            logger.info('\nGuest addition cancelled')
            return
            
if __name__ == '__main__':
    logger.debug('Welcome to guest adding program!')
    
    try:
        display_guests(FILENAME)
        add_guest('Add new guest: ')
        logger.info('Guest list updated!')
        
    except Exception as e:
        logger.error(f'An error occurred: {e}')