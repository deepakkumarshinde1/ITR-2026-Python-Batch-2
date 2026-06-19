# Handle

# text files
# .txt .csv .json => readable format
# binary files
# .jpg .gif .webp .pdf  .mp3 .exe .mp4=> 1010101


# File modes

# r => read file
# w => write file 
# a => append file
# x => create file is not exists
# r+ => read and write
# w+ => write and read
# a+ => append and read
# rb => read binary
# wb => write binary

# read
# f= open('students.txt','r')
# print(f.read())

# file error => if file not exists

# write
# f = open("hello.txt",'w')
# f.write("Hello, Smita")

# create a new file is file not exists

#append
# write
f = open("hello1.txt",'a')
f.write("\nHello, Smita")