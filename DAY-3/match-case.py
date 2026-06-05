# 1 => AI
# 2 => ML
# 3 => Java
# 4 => React
yourCourse = int(input("Kindly enter your course choice = "))

match yourCourse:
    case 1:
        print("Welcome to AI course.")
    case 2:
        print("Welcome to ML Course.")
    case 3:
        print("Welcome to Java Course.")
    case 4:
        print("Welcome to React Course.")
    case _:
        print("Invalid course choice.Please select from 1 to 4.")