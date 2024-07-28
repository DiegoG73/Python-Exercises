"""
Mostrar todos los números impares entre dos números que decida el usuario
"""


number1 = int(input("Inserte el primer número (debe ser menor que el segundo): "))
number2 = int(input("Inserte el primer número (debe ser mayor que el primero): "))


if number1 < number2:
    for number in range (number1, number2):
        if number % 2 != 0:
            print(f"{number} es impar")
else:
    print("El primer número debe ser menor al segundo")