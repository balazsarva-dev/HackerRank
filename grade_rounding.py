import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

def gradingStudents(grade: int) -> int:
    if grade > 37 and grade % 5 != 0:
        counter = grade
        while counter % 5 != 0:
            counter += 1
        result = counter - grade
        if result < 3:
            return counter
    return grade

def get_valid_integer(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                logger.warning(f'Please enter an integer between {min_value} and {max_value}.')
        except ValueError:
            logger.error('Invalid input. Please enter a valid integer.')

def main():
    n = get_valid_integer('Enter the number of students: ', 1, 60)
    for _ in range(n):
        grade = get_valid_integer('Enter the grade: ', 0, 100)
        rounded_grade = gradingStudents(grade)
        logger.info(f'Rounded Grade: {rounded_grade}')

if __name__ == '__main__':
    main()