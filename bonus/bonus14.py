from bonus.files.parser_functions import feet_extractor, feet_converter 

feet_inches = input("Enter feet and inches: ")


extracted = feet_extractor.extract(feet_inches)
result = feet_converter(extracted['feet'], extracted['inches'])

print(f"{extracted['feet']} feet and {extracted['inches']} inches is equal to {result}")

if result < 1: 
    print("kid is too small")
    
else:
    print("kid can go on the rollercoaster")