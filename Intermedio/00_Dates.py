### Dates ###

### Declaraciones
from datetime import datetime

### 

### Funciones
def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)

###

now = datetime.now()

print_date(now)

timestamp = now.timestamp()

print(timestamp)

year_2024 = datetime(2024, 1, 1)

print_date(year_2024)

###
from datetime import time, date

current_time = time(21, 6, 0)
current_date = date.today()

print("Time y Date")

print(current_date.year)
print(current_date.month)
print(current_date.day)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


