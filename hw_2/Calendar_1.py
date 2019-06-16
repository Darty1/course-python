import calendar

day, month, year = map(int, input("input data: ").split('.'))
print(calendar.weekday(year, month, day))
