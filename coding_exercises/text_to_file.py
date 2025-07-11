#create the following program

#1)Prompts user to enter a new member 
#2)Adds that member to members.txt at the end of the existing members
new_member = input("Add a new member: ")

#open file in read mode to initiate the list and prevent overriding
file = open("coding_exercises/members.txt","r")

#read in list format
members = file.readlines()

#close the file appropriately to avoid interference 
#The file will still be opened for mutations
file.close()

members.append(new_member)

file = open("coding_exercises/members.txt","w")

file.writelines(members)
file.close()

