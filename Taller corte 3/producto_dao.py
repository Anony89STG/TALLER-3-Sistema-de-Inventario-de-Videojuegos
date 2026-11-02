from Base_datos import BaseDatos
from modelo import Producto


class ProductoDAO:
    """Maneja el acceso a datos (CRUD) en SQLite para los productos."""

    def __init__(self):
    
        BaseDatos.crear_tabla()

    def insertar(self, producto: Producto) -> int:
        #Conectar y crear el cursor
        conexion = BaseDatos.conectar()
        cursor = conexion.cursor()
        
        #Ejecutar el INSERT de forma parametrizada
        cursor.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
            (producto.nombre, producto.precio, producto.stock)
        )
        
        
        conexion.commit()
        nuevo_id = cursor.lastrowid
        
        #Cerrar conexión y retornar el nuevo ID
        conexion.close()
        return nuevo_id

    def obtener_todos(self) -> list:
        #Conectar y ejecutar la consulta de todos los registros
        conexion = BaseDatos.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, precio, stock FROM productos")
        
        
        filas = cursor.fetchall()
        conexion.close()
        
        #Convertir cada fila tupla a un objeto Producto
        return [Producto(nombre=f[1], precio=f[2], stock=f[3], id=f[0]) for f in filas]

    def obtener_por_id(self, id_producto: int) -> Producto:
        #Conectar y buscar por ID
        conexion = BaseDatos.conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, nombre, precio, stock FROM productos WHERE id = ?",
            (id_producto,)
        )
        
        #Extraer la fila y cerrar la conexión
        fila = cursor.fetchone()
        conexion.close()
        
        #Retornar el objeto Producto si existe, o None
        if fila:
            return Producto(nombre=fila[1], precio=fila[2], stock=fila[3], id=fila[0])
        return None

    def actualizar(self, producto: Producto) -> bool:
        #Conectar y ejecutar la sentencia UPDATE
        conexion = BaseDatos.conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE productos SET nombre = ?, precio = ?, stock = ? WHERE id = ?",
            (producto.nombre, producto.precio, producto.stock, producto.id)
        )
        
        #Confirmar cambios y comprobar si se afectó alguna fila
        conexion.commit()
        actualizado = cursor.rowcount > 0
        
        #Cerrar la conexión y retornar el resultado
        conexion.close()
        return actualizado

    def eliminar(self, id_producto: int) -> bool:
        #Conectar y ejecutar la sentencia DELETE
        conexion = BaseDatos.conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        
        #Confirmar cambios y verificar si se eliminó
        conexion.commit()
        eliminado = cursor.rowcount > 0
        
        conexion.close()
        return eliminado
