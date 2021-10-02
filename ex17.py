from sys import argv
from os.path import exists
#make input from command line directly
#takes script python, file to copy from, file to copy to
script, from_file, to_file = argv
#printing to let user know we`ll copy from file1 to file2
print(f"Copying from {from_file} to {to_file}")

#We could do these two on one line, how?
in_file = open(from_file)
#The file that we`re goning to copy from is called now indata
indata = in_file.read()
#Measure the length of strings that indata contains
print(f"The input file is {len(indata)} bytes long")
#Check if the filr to copy to it exist or not, called to_file
print(f"Does the file output exist? {exists(to_file)}")
#Asking if exist or not do you want to continue?
print("Realy, hit RETURN to continue, or hit CTRL-C to abort.")
#Your decision
input()

#Open the file that we`re going to copy from indata file called to_file as 'w' write mode
out_file = open(to_file, 'w')
#Write the conents from indata to in_file 'the new file'
out_file.write(indata)
#print the process is succeded
print("Alright, all done")
#close the two files
out_file.close()
in_file.close()