import datetime as dt

# Current date and time
now = dt.datetime.now()
year = now.year
print(type(year))
print(now)
print(type(now))
print(now.weekday())

date_of_birth = dt.datetime(year=1986, month=2, day=17, hour=21)
print(date_of_birth)
