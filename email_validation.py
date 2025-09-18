from string import ( 
                    ascii_lowercase as lowers,
                    ascii_uppercase as uppers,
                    digits
                    )
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

username_chars = lowers+uppers+digits+'_-'
website_chars = lowers+uppers+digits
extension_chars = lowers+uppers

def validate(valid_chars: str, unexamined_string: str) -> str:
    '''
    Filters the unexamined_string to only include characters present in valid_chars.
    '''
    return ''.join(filter(lambda x: x in valid_chars, unexamined_string))

def fun(s: str) -> bool:
    '''
    Validates an email address based on specific criteria:
    '''
    if s.count('@') != 1 or s[0] == '@' or s[-1] == '@':
        return False
    user, rest = s.split('@')
    if '.' not in rest[-4:]:
        return False
    web, extension = rest.split('.')
    conditions = (username_chars, user), (website_chars, web), (extension_chars, extension)
    all_passes = all(validate(*condition) == condition[1] for condition in conditions)
    return len(extension) <= 3 and all_passes

def filter_mail(emails: list) -> list:
    return list(filter(fun, emails))

if __name__ == '__main__':
    try:
        n = int(input("Enter the number of emails: "))
        emails = [input("Enter email: ") for _ in range(n)]
        filtered_emails = filter_mail(emails)
        filtered_emails.sort()
        logger.info(f"Filtered emails: {filtered_emails}")
    except ValueError:
        logger.error("Invalid input. Please enter a valid number.")
