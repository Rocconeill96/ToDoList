#create a program that reads the three text files 
#a.txt
#b.txt
#c.txt

#1)reads each text file
#2)Print out the content of each file in the command line

filenames = ['coding_exercises/a.txt','coding_exercises/b.txt','coding_exercises/c.txt']

for filename in filenames:
    file = open(filename, "r")
    content = file.read()
    print(content)