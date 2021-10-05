import random
import datetime 
#print (random.randint(1000,9999))
dates=datetime.datetime.now()
print(dates)
current_date=dates.strftime("%Y-%m-%d %H:%M:%S")
print(current_date)
