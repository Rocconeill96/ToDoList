feet_inches = input("Enter feet and inches: ")

def extract(feet_and_inches):
    comps = feet_and_inches.split()
    
    if len(comps) < 2:
        raise IndexError("Invalid entry! Please enter a number for feet and inches. Remember to include a space between feet and inches")
    
    else:
        feet = float(comps[0])
        inches = float(comps[1])
    
    
    if inches > 11:
        raise ValueError("Inches can't be greater than 12!")
    
    elif inches < 0:
        raise ValueError("Inches can't be negative!")
    
    else:
        return {'feet':feet,'inches': inches}
    

def convert(feet, inches):
    
    metres = (feet * 0.3048) + (inches * 0.0254)
    
    return metres

extracted = extract(feet_inches)
result = convert(extracted['feet'], extracted['inches'])

print(f"{extracted['feet']} feet and {extracted['inches']} inches is equal to {result}")

if result < 1: 
    print("kid is too small")
    
else:
    print("kid can go on the rollercoaster")