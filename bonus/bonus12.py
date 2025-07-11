
feet_inches = input("Enter feet and inches: ")

def convert(feet_inches):
    comps = feet_inches.split(" ")
    feet = float(comps[0])
    inches = float(comps[1])
    
    if inches > 11:
        raise ValueError("Inches can't be greater than 12!")
    
    elif inches < 0:
        raise ValueError("Inches can't be negative!")
    
    else:
        
    
        metres = (feet * 0.3048) + (inches * 0.0254)
    
    return metres


result = convert(feet_inches)

if result < 1: 
    print("kid is too small")
    
else:
    print("kid can go on the rollercoaster")