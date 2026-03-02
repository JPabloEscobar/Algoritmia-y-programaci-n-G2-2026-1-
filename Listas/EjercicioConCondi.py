"""
En una empresa se necesita registrar la entrada y salida
de us trabajadores que estan compuestos por una coleccion
de cinco personas, en caso de que una persona no sea parte
de la base de datos mandar un mensaje de rachazo a la entrada.
"""

bd = {"Pepito", "Pepita", "Jasinto", "Ruberto", "Daniel"}
i = input("Ingrese su nombre: ")

if i in bd:
    t = input("Usted entra o sale? (E/S): ")
    if t == "E":
        h = int(input("Ingrese la hora de entrada: "))
        print(f"{i} ingresaste a las {h}am")
    elif t == "S":
        h = int(input("Ingrese la hora de salida: "))
        print(f"{i} saliste a las {h}pm")
    else:
        print("Usted no es de aqui, vallase porfavor")