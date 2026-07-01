from datetime import datetime,timedelta

today = datetime.now()
exam_date = today + timedelta(days=20)

prevDate = today - timedelta(days=20)
print(exam_date)
print(prevDate)



exam_date = datetime(2026,7,29)

_exam_date_days = exam_date - today
print(_exam_date_days.days)


# calc age
year = 2008 
#int(input("Enter dob year : "))
age = today.year - year
print(f"age of rohit is {age}")


# check attendance
hr = today.hour

if hr < 9:
    print("Regular")
elif hr < 12:
    print("Late")
elif hr < 15:
    print("half day")
else:
    print("Absent")