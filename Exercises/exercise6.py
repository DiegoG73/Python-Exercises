"""
    Calcular el porcentaje de x número
    Ejemplo: x% de 35
"""

number = float(input("Introduce el número del que quieres sacar un porcentaje: "))
percentage = float(input("Introduce el porcentaje que quieres calcular del primer número dado: "))

calculate = percentage * (number/100)
print(calculate)