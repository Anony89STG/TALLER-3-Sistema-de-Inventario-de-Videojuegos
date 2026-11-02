from producto_servicio import ProductoServicio


def leer_entero(mensaje: str) -> int:
    # Solicitar un entero y repetir hasta que la entrada sea válida
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero válido.")


def leer_flotante(mensaje: str) -> float:
    
    while True:
        try:
            return float(input(mensaje).strip())
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un valor numérico válido.")


def mostrar_menu():
    # Desplegar las opciones disponibles en consola
    print("\n" + "=" * 50)
    print("   SISTEMA DE INVENTARIO DE VIDEOJUEGOS (DAO)")
    print("=" * 50)
    print("1. Registrar videojuego")
    print("2. Mostrar inventario")
    print("3. Buscar videojuego por ID")
    print("4. Actualizar videojuego")
    print("5. Eliminar videojuego")
    print("6. Vender unidades")
    print("7. Salir")
    print("=" * 50)


def ejecutar_aplicacion():
    
    servicio = ProductoServicio()

    # Paso 2: Ciclo principal interactivo de la consola
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()

        try:
            
            if opcion == "1":
                print("\n--- REGISTRAR VIDEOJUEGO ---")
                nombre = input("Nombre del videojuego: ")
                precio = leer_flotante("Precio: ")
                stock = leer_entero("Cantidad disponible (stock): ")
                producto = servicio.registrar_producto(nombre, precio, stock)
                print(f"Producto guardado correctamente: {producto}")

            
            elif opcion == "2":
                print("\n--- INVENTARIO ACTUAL ---")
                productos = servicio.listar_productos()
                if not productos:
                    print("El inventario está vacío actualmente.")
                else:
                    for prod in productos:
                        print(prod)

            
            elif opcion == "3":
                print("\n--- BUSCAR VIDEOJUEGO ---")
                id_prod = leer_entero("Ingrese el ID del videojuego: ")
                producto = servicio.buscar_producto(id_prod)
                print(f"Videojuego encontrado -> {producto}")

            
            elif opcion == "4":
                print("\n--- ACTUALIZAR VIDEOJUEGO ---")
                id_prod = leer_entero("Ingrese el ID del videojuego a actualizar: ")
                actual = servicio.buscar_producto(id_prod)
                print(f"Datos actuales -> {actual}")

                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_precio = leer_flotante("Nuevo precio: ")
                nuevo_stock = leer_entero("Nuevo stock: ")

                actualizado = servicio.actualizar_producto(
                    id_prod, nuevo_nombre, nuevo_precio, nuevo_stock
                )
                print(f"Videojuego actualizado correctamente: {actualizado}")

            
            elif opcion == "5":
                print("\n--- ELIMINAR VIDEOJUEGO ---")
                id_prod = leer_entero("Ingrese el ID del videojuego a eliminar: ")
                servicio.eliminar_producto(id_prod)
                print(f"El videojuego con ID {id_prod} fue eliminado del inventario.")

           
            elif opcion == "6":
                print("\n--- VENDER UNIDADES ---")
                id_prod = leer_entero("Ingrese el ID del videojuego a vender: ")
                cantidad = leer_entero("Ingrese la cantidad de unidades a vender: ")
                producto = servicio.vender_unidades(id_prod, cantidad)
                print(
                    f"Venta realizada con éxito. Nuevo stock de '{producto.nombre}': "
                    f"{producto.stock} unidades."
                )

            
            elif opcion == "7":
                print("\nSaliendo del sistema. ¡Hasta pronto!")
                break

            else:
                print("Opción no válida. Por favor, elija un número entre 1 y 7.")

        # Manejo de excepciones esperadas de negocio y entrada
        except (ValueError, LookupError) as error:
            print(f"Error: {error}")
        except Exception as error_inesperado:
            print(f"Ocurrió un error inesperado: {error_inesperado}")


# Punto de entrada de la aplicación
if __name__ == "__main__":
    ejecutar_aplicacion()
