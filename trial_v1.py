import logging
import sys
from typing import Optional, Generator, Tuple

logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

FILENAME = 'guest_list.txt'

def read_guests_from_file(file_name: str) -> Generator[Tuple[Optional[str], Optional[str]], None, None]:
    if not file_name:
        yield None, 'File name is missing! '
        return
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if line := line.strip(): 
                    yield line, None
    except FileNotFoundError:
        yield None, 'File not found! '
    except IOError:
        yield None, f'Error reading from {file_name}! '
    except Exception as e:
        yield None, f'An error occurred: {e}! '
        
def add_data_to_a_file(file_name: str, data: str) -> bool:
    if not all([file_name, data]):
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
    if not file_name:
        logger.error('File name is missing! ')
        return
    logger.info('\nGuest list: \n')
    for data, error in read_guests_from_file(file_name):
        logger.error(error) if error else logger.info(data)

def validate_guest() -> Generator:
    while True:
        try:
            guest_input = yield
            if not guest_input or len(guest_input.split()) != 2:
                yield None, 'Please enter guest name and age! '

            name, age = guest_input.split()
            if not name.isalpha():
                yield None, 'Name must be alphabetic! '

            try:
                int_age = int(age)
                if int_age not in range(18, 101):
                    yield None, 'Age must be between 18 and 100! '
                yield f'{name},{int_age}', None
            except ValueError:
                yield None, 'Age must be number! '
        except Exception as e:
            yield None, f'An error occurred: {e}! '
        
def add_guest(prompt: str) -> None:
    guest_validator = validate_guest()
    next(guest_validator)

    while True:
        try:
            new_guest = input(prompt)
            if new_guest.lower() == 'cancel':
                return logger.info('Operation cancelled! ')

            data, error = guest_validator.send(new_guest)
            if error:
                logger.error(error)
                guest_validator = validate_guest()
                next(guest_validator)
                continue

            if data and add_data_to_a_file(FILENAME, data):
                return logger.info('Guest added successfully to the file!')

        except KeyboardInterrupt:
            return logger.info('\nGuest addition cancelled')

if __name__ == '__main__':
    logger.debug('Welcome to guest adding program!')
    while True:
        try:
            number_of_adding_guests = int(input('Enter the number of guests to add (1-5): '))
            if number_of_adding_guests in range(1, 6):
                break
            logger.error('Invalid range! Enter a number between 1 and 5! ')
        except ValueError:
            logger.error('Invalid input! Enter an integer! ')

    for _ in range(number_of_adding_guests):
        try:
            add_guest('Add new guest (name age) or enter "cancel": ')
        except Exception as e:
            logger.error(f'An error occurred: {e}')
    display_guests(FILENAME)