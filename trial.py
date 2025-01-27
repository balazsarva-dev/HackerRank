import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(levelname)s - %(message)s')
logger.addHandler(stream_handler)

def read_data_from_a_file(file_name: str) -> list:
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        logger.error('File not found! ')
        return []

def display_guests(file_name: str) -> None:
    if guests := read_data_from_a_file(file_name):
        logger.info('Guest list:\n')
        for guest in guests:
            logger.info(guest.strip())
    
def add_data_to_a_file(file_name: str, data: str) -> None:
    try:
        with open(file_name, 'a') as file:
            file.write('\n')
            file.write(data)
        logger.info('Guest added successfully!')
    except IOError:
        logger.error(f'Error writing to {file_name}! ')

def add_guest(prompt: str, file_name: str) -> None:
    while True:
        new_guest = input(prompt).split()
        
        if 'quit' in new_guest:
            logger.info('Operation cancelled! ')
            return
        
        if len(new_guest) != 2:
            logger.error('Invalid input! Name and age must be entered! Try again! ')
            continue
        
        name = new_guest[0].title()
        if not name.isalpha():
            logger.error('Name must be alphabetic! ')
            continue
        
        try:
            age = int(new_guest[1])
            if age < 18:
                logger.error('Guest must be 18 years old or above! ')
                continue
            add_data_to_a_file(file_name, f'{name},{age}')
            return

        except ValueError:
            logger.critical('Age must be number! ')

def main():
    FILENAME = 'guest_list.txt'
    display_guests(FILENAME)
    prompt = 'Enter guest name and age separated by space or "quit"!: '
    add_guest(prompt, FILENAME)

if __name__ == '__main__':
    main()