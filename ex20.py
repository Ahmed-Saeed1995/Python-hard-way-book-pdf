from sys import argv

script , input_file = argv
#Define a function that print all the lines
def print_all(f):
    print(f.read())
#define a function that remove the curcer in the begining of the file
def rewind(f):
    f.seek(0)
#define the function that print each line one by one
def print_a_line(line_count,f):
    print(line_count,f.readline())

#open the function that got from script 'input from command line'
current_file =open(input_file)

#A message to print all content in the file
print("First let`s print the whole file:\n ")
#call the functio that print the content of file
print_all(current_file)

#Remove the curser at the begunung of the file
print("Now let`s rewind, kind of like a tape")
rewind(current_file)

#A message to print the line one by one
print("Let`s print three lines:")

#assingn a vriable to show how many lines printed 
current_line = 1
#call the function that print the line one by one
print_a_line(current_line, current_file)

#process of calling a function to print the second line
current_line += 1
print_a_line(current_line, current_file)

#print third line by function readline()
current_line += 1
print_a_line(current_line, current_file)

""" current line is a any normal variable and in this case
it doesn`t related to anything at all, it just tellthe user 
how many lines printed manually"""

""" as we can check by removing current_line to prove it doesn`t really related to 
anything by calling the function print_a_line it prints readline() function
and how many call the function print_a_line == how many lines actully in the file writen
as conclusion readline() print one line when calling the function again
the curcer is seek at the end of the first line after calling it continue to printthe next line
in the content infront of the curser"""
