
import datetime # it's okay to import like this

# 3-1-2015
# day.weekday() mon = 0, tues = 1, wed = 2, thurs = 3, fri = 4, sat = 5, sun = 6

day = datetime.datetime(year=2004, month=3, day=1) # order does not matter for keyword arg (kwarg)
print(day - datetime.timedelta(hours=12))

now = datetime.datetime.now()
print(now)
now_formatted = now.strftime("%A, %B %d %Y %H:%M:%S") #the purpose of strftime is to make the time more readable
print(now_formatted)

now_obj = datetime.datetime.strptime(now_formatted, "%A, %B %d %Y %H:%M:%S")
print(type(now_obj))
print(now_obj)

now_formatted = now.strftime("%A, %B %d %Y %H:%M:%S")
