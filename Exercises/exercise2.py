"""
Escribir un programa que muestre los cuadrados de los 60 primeros números naturales. Resolverlo con for y while
"""

print("Bucle For")
for i in range (1,61):
    print(i ** 2)


print("\nBucle While")
counter = 0
while counter <= 60:
    square = counter * counter
    counter += 1
    print(square)