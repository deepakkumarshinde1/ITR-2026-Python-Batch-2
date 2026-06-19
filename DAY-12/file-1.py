file = open("student.txt","w")
file.write("\nDeepak")
file.write("\nSai")
file.write("\nSham")
file.write("\nNeha")
file.write("\nArun")
file.write("\nAnil")
file.close()

# file statement
with open('user.log',"w") as file:
    file.write("User have login successfully")