from sys import argv
#Assining a vriaable from module sys
script, filename = argv
#printing a banner to tell the user to read the file or cancel the program
print(f"We`re going to erase {filename}.")
print("If you don`t want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
#An inprut for user`s dicision
input("?")
#printing to know the user the file will open
print("Opening the file.....")
#opening file
target = open(filename,'w')

#What is that Truncate means?
print("Truncate the file. Goodbye!")
target.truncate()
#the file stops at this point if I remove the character 'w'
#If i remove Truncate and 'w' the file stops at open(filename) and gives us an Error

#A message to get 3 unputs from user
print("Now I`m going to ask you for three lines.")
#Got three input from user
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#printing to user that the inputs we`ve got from user will write in file
print("I`m going to write these to the file.")
#Writing user`s inputs imto the file by using string formats in one line
target.write(f"{line1},\n{line2},\n{line3}\n")
"""
#Writing user`s inputs into the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""
#Close the file after a message to let the user know
print("And finally. We close it.")
target.close()