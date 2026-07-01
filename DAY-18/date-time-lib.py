from datetime import datetime,date

# --- modules --
# data
# time
# datetime
# timedelta
# timezone

now = datetime.now()
# print(now) # 2026-06-24 11:08:18.002366 # yyyy-mm-dd
today = date.today() # yyyy-mm-dd
# print(today)

time = datetime.now().time()
# print(time)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

newDate = now.strftime('%A,%B,%d:%m/:%Y') # 24/06/2026
# print(newDate)
newTime = now.strftime('%I:%M:%S') # 11:27:53
print(newTime)
# %d = Day
# %m = Month
# %Y = Full Year
# %y = Short Year
# %A = Day Name
# %B = Month Name
# %H = 24 hrs
# %I = 12 hrs
# %S = Sec
# %M = Min