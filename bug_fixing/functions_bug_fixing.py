def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum
#original error: function WAS NOT returning a value due to the no return clause
    
celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32
print(fahrenheit)