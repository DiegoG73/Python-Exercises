"""
Hacer un programa que muestre todos los numeros entre dos numeros que diga el usuario:
"""

number1 = int(input("Introduce el primer número: "))
number2 = int(input("Introduce el segundo número: "))

for number in range(number1 + 1, number2):
    print(number)