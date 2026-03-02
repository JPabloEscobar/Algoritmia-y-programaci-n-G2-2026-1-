Lista = [1, 2.3, "Hola", True]

agregar = Lista.append("Mundo") #agregar un elemento al final de la lista
agregar2 = Lista.insert(1, "Python") #agregar un elemento en la posición 1 de la lista
quitar1 = Lista.remove(2.3) #quita la "variable" 2.3 de la lista
quitar2 = Lista.pop(0) #quita el elemento en la posición 0 de la lista si no se quita el último elemento de la lista

print(Lista)

Diccionario = {"numero": 1,
                2: "dos",
                2.3: True}

print(Diccionario["numero"]) #imprime el valor de la clave (key) "numero"
