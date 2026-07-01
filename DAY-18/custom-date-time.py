from datetime import date,time,datetime
# date
newDate =  date(2026,1,26)
newDate = newDate.strftime('%d,%B %Y')
print(newDate) #26,January 2026

# time
newTime = time(14,30,30)
newTime = newTime.strftime('%I:%M:%S')
print(newTime) # 02:30:30

# date & time
newDateTime = datetime(2026,1,26,14,30,30);
print(newDateTime) #2026-01-26 14:30:30




# date calc
# json
# pip
# api calling ( request )