"""Python script from exercise 17 short code"""

from sys import argv

script, file1,file2 = argv

infile = open(file1,'r')
copyed_file = open(file2, 'w')
copyed_file.write(infile.read())
print("All Done")