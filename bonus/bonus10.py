

try:
    width = float(input("Please enter a width (cm): "))
    length = float(input("Please enter a length (cm): "))
    
    if width == length: 
        exit("That looks like a square!")
        
    
    area = width * length 
    print("Successful inputs! Your area calculated below...")
    print(f"{width}cm * {length}cm = {area}cm^2")
    
except ValueError:
    print("Please enter a number in the form of a float!")