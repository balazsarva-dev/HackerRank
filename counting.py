import time

def enter_name() -> str:
    while True:
        name = input('What is your name? ')
        if not name:
            print('Please enter a valid name! ')
        elif name.isalpha():
            return name.title()
        else:
            print('Only alphabetic character is valid! ')

def countdown(seconds: int, feature : str, feature_value : any) -> None:
    print(f'Your {feature} appear in')
    while seconds > 0:
        print(f'{seconds}...')
        seconds -= 1
        time.sleep(1)
    print(f'Time is up! Your {feature} is: {feature_value} ')
    
def main() -> None:
    enter_your_name = enter_name()
    countdown(seconds=5, feature='name', feature_value=enter_your_name)
    print('Goodbye! ')

if __name__ == '__main__':
    main()