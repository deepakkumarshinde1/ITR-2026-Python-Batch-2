password = "admin@123"
userPassword = ""
attempt = 0
while userPassword != password:
    if(attempt > 2):
        print("you have done max 3 attempt, try after 1 hr")
        break
    attempt += 1
    userPassword = input("Enter your password = ")

if attempt != 3 and password == userPassword:    
    print("Login successfully")