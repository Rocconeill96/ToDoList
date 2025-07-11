password = input("Enter a new password:")

#empty dictionary variable
result = {}

#checking password length
if len(password) >= 8:
    result["length"] = True
    
else:
    result["length"] = False
 
#initialising variables numbers and uppercase that by default are false 
digit = False   
uppercase = False

#looping though each string element to assess if a number is there and returning true if so
for i in password: 
    #if statement by default will check if condition is == True unless declared otherwise
    if i.isdigit():
        digit = True
        
result["digits"] = digit     

#looping through string input to assess whether there is upper case letters and returning true if so 
for i in password: 
    if i.isupper():
        uppercase = True
        
result["upper-case"] = uppercase
        
    

#if condition that assesses if all list elements are True and thus "strong password"

if all(result.values()):
    print("Strong password!")
    
else:
    print("Weak password!")