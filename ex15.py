from sys import argv
#making to input got from command line before excute the code
script, filename = argv
#open the file that passed from command line
txt = open(filename)
#A note before reading file
print(f"Here`s your file {filename}:")
#Reading file {filename} content
print(txt.read())
#A message of opening another file from the user`s choice
print("Type the filename again:")
#Get input from user the name of the file.extension
file_again = input('>')
#opening that file that got from the user.
txt_again = open(file_again)
#Finally read that file
print(txt_again.read())
txt_again.close()