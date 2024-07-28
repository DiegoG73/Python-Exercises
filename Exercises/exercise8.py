"""
Un programa que pida la calificación de 15 alumnos y sacar por pantalla cuántos han aprobado y cuántos han reprobado
"""
counter = 1
while counter <= 15:
    qualification = int(input("Introduce la calificaión del 0 al 100:"))
    
    if qualification <= 50:
        print("Lo siento, Pepito Juarez, has R E P R O B A D O")
    else:
        print("Felicidades, eres un GENIOUS!")
    counter += 1