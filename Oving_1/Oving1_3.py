import math

radius = float(input('Skriv inn radius: '))

volum = (4*math.pi*radius**3)/3
overflate = 4*math.pi*radius**2

print('Overflaten til en sirkel med radius', radius, 'er', math.ceil(overflate*100)/100)
print('Volumet blir:', math.ceil(volum*100)/100)
