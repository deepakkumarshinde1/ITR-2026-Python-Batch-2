# if else
doIhaveMoney = False
if doIhaveMoney == True:
    print("I am happy :)")
else:
    print("I am sad :(")

# chain if else

marks = 36
if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("1st class")
elif marks >= 40:
    print("2nd class")
else:
    print("Fail")

    

# nested if else 
isGuestLogin = False

if isGuestLogin == True:
    print("Welcome to free web series")
else:
    userType = "P"
    if userType == "S":
        print("Welcome to paid but ads plus web series")
    else:
        print("Welcome to paid and ads free web series")
