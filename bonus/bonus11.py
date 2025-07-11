def get_average():
    with open("bonus/files/data.txt", "r") as file:
        data = file.readlines()
        
    values = [float(item.strip()) for item in data if item.strip().isdigit()]
    average_local = sum(values)/len(values)
    return average_local

avg = get_average()
print(avg)