from sys import argv

script, filename = argv

print("Do you want to open the file ?")
print("If so press OK, if not hit CTRL-C (^C)")

input("What did you decide? ")

file = open(filename,'r')

print("The file contains: \n")
content = file.read()
print(content)

print("Are you sure that you want close the file.? ")

input("Your decision? ")
file.close()