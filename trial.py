import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(levelname)s - %(message)s')
logger.addHandler(stream_handler)

def read_file(file_name: str) -> list:
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        logger.error('File not found! ')
        return []
    
def write_file(file_name: str, data: list) -> None:
    try:
        with open(file_name, 'w') as file:
            file.writelines(data)
        logger.info('Data written successfully! ')
    except IOError:
        logger.error(f'Error writing to {file_name}! ')

def add_guest(prompt: str, guest_list: list) -> list:
    while True:
        new_guest = input(prompt).split()
        if len(new_guest) != 2:
            logger.error('Invalid input! Only name and age is allowed! Try again! ')
            continue
        name = new_guest[0]
        if all(char.isalpha() for char in name):
            try:
                age = int(new_guest[1])
                if age < 18:
                    logger.error('Guest must be 18 years old or above! ')
                    continue
                result = f'{name},{age}'
                guest_list.append(result+'\n')
                logger.info('Guest added successfully! ')
                logger.info(result)
                return guest_list
            except ValueError:
                logger.critical('Age must be number! ')
        else:
            logger.error('Name must be alphabetic! ')
            continue

if __name__ == '__main__':
    logger.debug('Welcome to guest adding program! ')
    glist = read_file('guest_list.txt')
    new_guest = add_guest('Enter the new guest name and age! ', glist)
    write_file('guest_list.txt', ''.join(new_guest))
    logger.info('\nGuest list: \n')
    for val in read_file('guest_list.txt'):
        logger.info(val.strip())