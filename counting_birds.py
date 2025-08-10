from collections import Counter
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def migratoryBirds(arr):
    count_types_of_birds = Counter(arr)
    max_value = max(count_types_of_birds.values())
    result = min(key for key in count_types_of_birds if count_types_of_birds[key] == max_value)
    logger.info(f'Most common bird type: {result}')
    return result

def get_bird_sightings():
    while True:
        try:
            arr_count = int(input("Enter the number of bird sightings: ").strip())
            if arr_count in range(1, 100):
                return arr_count
            logger.error("Invalid input! Please enter an integer between 1 and 99.")
        except ValueError:
            logger.error("Invalid input! Please enter an integer between 1 and 99.")

def main():
    number_of_observations = get_bird_sightings()
    while True:
        try:
            arr = list(map(int, input("Enter the bird types: ").rstrip().split()))
            if len(arr) == number_of_observations:
                return migratoryBirds(arr)
            logger.error("Invalid input! Please enter exactly {} integers.".format(number_of_observations))
        except ValueError:
            logger.error("Invalid input! Please enter integers only.")

if __name__ == '__main__':
    main()