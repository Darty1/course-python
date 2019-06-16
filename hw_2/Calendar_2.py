import calendar

day_otw = int(input("0 - Monday "
                "1 - Tuesday "
                "2 - Wednesday "
                "3 - Thursday "
                "4 - Friday "
                "5 - Saturday "
                "6 - Sunday "))
day = 1
month = 6
yeahr = 2019
while True:
    if month < 1:
        month = 12
        yeahr -= 1
    if calendar.weekday(yeahr, month, day) == day_otw:
        print(month, '.', yeahr)
        break
    month -= 1
