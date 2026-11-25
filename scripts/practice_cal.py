import calendar

while True:
    try:
        date_inputs = list(map(int, input().split()))
        if len(date_inputs) != 3:
            print('Invalid input! You must enter day, month, year! ')
            continue
        month, day, year = date_inputs
        if  month in range(1, 13) and day in range(1, 32) and year in range(2000, 3001):
            days = dict(enumerate(['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']))
            print(days[calendar.weekday(year, month, day)])
            break
        print('Invalid input! The day must be in the range of 1 to 31, the month must be in the range of 1 to 12, and the year must be in the range of 2000 to 3000! ')
    except ValueError:
        print('Invalid input! You must enter integers! ')