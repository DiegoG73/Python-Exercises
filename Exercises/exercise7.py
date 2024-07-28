"""
Hacer un programa que pida números al usuario indefinidamente hasta meter el número 111
"""

counter = 0

while counter < 100:
    number = int(input("Adivina el número: "))
    
    if number == 111:
        break
    else:
        print(f"Has introducido el número: {number}")