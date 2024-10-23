productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    try:
        precio = float(input("Introduce el precio del producto: "))
        cantidad = int(input("Introduce la cantidad del producto: "))
        productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })
        print(f"Producto '{nombre}' añadido correctamente.")
    except ValueError:
        print("Error: El precio y la cantidad deben ser valores numéricos.")

def ver_productos():
    if productos:
        print("Lista de productos:")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos en el inventario.")

def actualizar_producto():
    ver_productos()
    nombre_producto = input("Introduce el nombre del producto que deseas actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre_producto:
            try:
                nuevo_nombre = input("Introduce el nuevo nombre (presiona Enter para mantener el actual): ") or producto['nombre']
                nuevo_precio = input("Introduce el nuevo precio (presiona Enter para mantener el actual): ")
                nuevo_precio = float(nuevo_precio) if nuevo_precio else producto['precio']
                nueva_cantidad = input("Introduce la nueva cantidad (presiona Enter para mantener la actual): ")
                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else producto['cantidad']

                producto.update({"nombre": nuevo_nombre, "precio": nuevo_precio, "cantidad": nueva_cantidad})
                print(f"Producto '{nombre_producto}' actualizado correctamente.")
            except ValueError:
                print("Error: El precio y la cantidad deben ser valores numéricos.")
            break
    else:
        print(f"El producto '{nombre_producto}' no fue encontrado.")

def eliminar_producto():
    ver_productos()
    nombre_producto = input("Introduce el nombre del producto que deseas eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre_producto:
            productos.remove(producto)
            print(f"Producto '{nombre_producto}' eliminado correctamente.")
            break
    else:
        print(f"El producto '{nombre_producto}' no fue encontrado.")

def guardar_datos():
    try:
        with open("productos.txt", "w") as file:
            for producto in productos:
                file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def cargar_datos():
    try:
        with open("productos.txt", "r") as file:
            for linea in file:
                nombre, precio, cantidad = linea.strip().split(", ")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("Archivo de productos no encontrado, iniciando con inventario vacío.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")

def menu():
    cargar_datos()
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()
