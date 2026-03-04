#TODO: Implemente los ejercicios para de listas y condicionales.
"""
 1.Una empresa de transporte tiene una lista con los nombres de sus conductores.
   Se pide realizar un programa que permita ingresar el nombre de un conductor y 
   verificar si se encuentra en la lista.

 2. Una empresa de energía quiere llevar un registro de sus clientes y su consumo
    de energía. Se pide realizar un programa que permita ingresar el nombre del 
    cliente y su consumo en kWh, y luego calcular el costo total a pagar considerando
    que el precio por kWh es de $0.15. 

 3. Una tienda tiene en su base de datos los siguientes productos:
     ______________________
     | Producto  | Precio |
     |-----------|--------|
     | Manzana   | $2.5   |
     | Banana    | $1.8   |
     | Naranja   | $3.0   |
     | Pera      | $2.0   |
     | Monster   | $5.0   |
     | Agua      | $1.0   |
     | Coca-Cola | $3.5   |
     |--------------------|
    
     La propretaria de la tienda le necesita un sistema que le ayude a gestionar
     su inventario. El sistema debe permitirle: verificar si un producto se 
     encuentra en el inventario, agregar nuevos productos con su precio, eliminar
     productos y actualizar el precio de un producto existente.
"""
#1.
# conductores = ["Juan", "Maria", "Pedro", "Luisa", "Carlos"]
# nombre_conductor = input("Ingrese el nombre del conductor: ")
# if nombre_conductor in conductores:
#     print(f"El conductor {nombre_conductor} se encuentra en la lista.")
# else:
#     print(f"El conductor {nombre_conductor} no se encuentra en la lista.")

#2.
# clientes = {}
# nombre_cliente = input("Ingrese el nombre del cliente: ")
# consumo_kwh = float(input("Ingrese el consumo en kWh: "))
# costo_total = consumo_kwh * 0.15
# clientes[nombre_cliente] = consumo_kwh
# print(f"El cliente {nombre_cliente} tiene un consumo de {consumo_kwh} kWh y debe pagar ${costo_total:.2f}.")

#3.
inventario = {
    "manzana": 2.5,
    "banana": 1.8,
    "naranja": 3.0,
    "pera": 2.0,
    "monster": 5.0,
    "agua": 1.0,
    "coca-cola": 3.5
}

pedido = input("Que conocer del inventario?").lower()
if pedido in inventario:
    print(f"Hay del producto {pedido} y vale ${inventario[pedido]} por unidad.")
    desi = input("¿Qué desea hacer? (agregar/eliminar): ").lower()
    if desi == "agregar":
        nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
        precio_producto = float(input("Ingrese el precio del nuevo producto: "))
        inventario[nuevo_producto] = precio_producto
        print(f"Producto {nuevo_producto} agregado con precio ${precio_producto:.2f}.")
    elif desi == "eliminar":
        eliminar_producto = input("Ingrese el nombre del producto a eliminar: ").lower()
        if eliminar_producto in inventario:
            #inventario.pop(eliminar_producto)
            del inventario[eliminar_producto]
            print(f"Producto {eliminar_producto} eliminado del inventario.")
        else:
            print(f"El producto {eliminar_producto} no se encuentra en el inventario.")
      
else:
    print(f"No hay producto {pedido} en el inventario de la tienda.")