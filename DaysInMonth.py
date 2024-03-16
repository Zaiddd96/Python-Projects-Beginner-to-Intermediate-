def is_leap(year):
  """Checks the year is leap year or not!""" #Docstrings
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
  """returns how many days are in a month!"""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month-1]

year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year,month)
print(days)