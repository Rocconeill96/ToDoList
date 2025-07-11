filenames = ['doc.txt','report.txt','presentation.txt']

#create a program that 

#1)Generates multiple text files by iterating over the filenames list

#2)and writes the text Hello inside each generated text file

for filename in filenames:
    file = open(f"coding_exercises/{filename}", "w")
    file.write("Hello")
    file.close()