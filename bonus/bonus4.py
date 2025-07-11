#Whilst lists are mutable, strings ARE NOT
#So we need to use the .replace() method
filenames = ["1.Raw Data.txt", "2.Reports.txt","3.Presentations.txt"]

#looping through the list 

for filename in filenames:
    filename = filename.replace(".","-",1) #Number represents how the positional occurence to replace e.g. 1 = the first occurence of the string to be replaced
    print(filename)

