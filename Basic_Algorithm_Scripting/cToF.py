# Algorithm to convert temperature in celcius to fahrenheit

def convertToF(celcius):
    fahrenheit = celcius * (9 / 5) + 32
    return fahrenheit

print(convertToF(-30))
print(convertToF(30))
print(convertToF(20))
print(convertToF(0))