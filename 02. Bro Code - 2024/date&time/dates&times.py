import datetime

date = datetime.date(year=2025, month=1, day=2)
today = datetime.date.today()
time = datetime.time(hour=12, minute=30, second=0)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %d-%m-%y")

print(date)
print(today)
print(time)
print(now)
print()

target_datetime = datetime.datetime(year=2030, month=1, day=2, hour=12, minute=30, second=1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")