"""
Mostrar todas las tablas de multiplicar del 1 al 10. 
Mostrando el título de la tabla y luego las multiplicaciones (del 1 al 10)
"""

for header in range(1,11):
    print("#################################")
    print(f"########## Tabla del {header} ###########")
    print("#################################")
    
    for number in range(1,11):
        print(f"{number} x {header} = {number * header}")
    print("\n")