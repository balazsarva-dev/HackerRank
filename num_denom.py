from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x*y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input('Enter the number of fractions: '))):
        while True:
            inputs = list(input('Enter the numerator and the denominator! ').split())
            if len(inputs) == 2:
                try:
                    fracs.append(Fraction(*map(int, inputs)))
                    break
                except ValueError:
                    print('Only integers are allowed! Try again! ')
            else:
                print('You need to input two integers! Try again! ')
    result = product(fracs)
    print(*result)