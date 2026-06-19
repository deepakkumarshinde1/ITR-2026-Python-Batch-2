import os

isFileExists = os.path.exists('user.log')
# Whether the file exists or not.

if isFileExists == True:
    os.rename("user.log", "user-log.log")
    # Rename can use to rename the file.


if os.path.exists('student-copy.txt'):
    os.remove('student-copy.txt')
    # Remove can use to remove the file.