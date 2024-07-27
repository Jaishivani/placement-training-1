import calendar

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
month, day, year = map(int, input().split())

weekday = calendar.weekday(year, month, day)
print(days[weekday])
