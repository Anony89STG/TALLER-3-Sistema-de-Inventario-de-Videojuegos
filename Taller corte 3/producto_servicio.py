from modelo import Producto
from producto_dao import ProductoDAO


class ProductoServicio:
    """Contiene la lógica de negocio y validaciones del inventario."""

    def __init__(self):
        # Inicializar el objeto DAO para interactuar con la base de datos
        self.dao = ProductoDAO()

    def _validar_datos_producto(self, nombre: str, precio: float, stock: int):
        # Validar reglas de negocio básicas.
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del videojuego no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        if stock < 0:
            raise ValueError("La cantidad en inventario (stock) no puede ser negativa.")

    def registrar_producto(self, nombre: str, precio: float, stock: int) -> Producto:
        # Paso 1: Validar que los datos sean coherentes
        self._validar_datos_producto(nombre, precio, stock)
        
        # Paso 2: Crear el objeto Producto en memoria
        nuevo_producto = Producto(nombre=nombre.strip(), precio=precio, stock=stock)
        
        # Paso 3: Guardar en la base de datos y asignar el nuevo ID generado
        nuevo_producto.id = self.dao.insertar(nuevo_producto)
        return nuevo_producto

    def listar_productos(self) -> list:
      
        return self.dao.obtener_todos()

    def buscar_producto(self, id_producto: int) -> Producto:
        
        producto = self.dao.obtener_por_id(id_producto)
        if not producto:
            raise LookupError(f"No existe ningún videojuego registrado con el ID {id_producto}.")
        return producto

    def actualizar_producto(self, id_producto: int, nuevo_nombre: str, nuevo_precio: float, nuevo_stock: int) -> Producto:
        
        producto_existente = self.buscar_producto(id_producto)
        self._validar_datos_producto(nuevo_nombre, nuevo_precio, nuevo_stock)

        
        producto_existente.nombre = nuevo_nombre.strip()
        producto_existente.precio = nuevo_precio
        producto_existente.stock = nuevo_stock

        self.dao.actualizar(producto_existente)
        return producto_existente

    def eliminar_producto(self, id_producto: int) -> None:
        self.buscar_producto(id_producto)
        #Eliminar el registro en la BD
        self.dao.eliminar(id_producto)

    def vender_unidades(self, id_producto: int, cantidad: int) -> Producto:
       
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")

        #Buscar el producto y validar que haya stock suficiente
        producto = self.buscar_producto(id_producto)
        if cantidad > producto.stock:
            raise ValueError(
                f"Stock insuficiente para '{producto.nombre}'. "
                f"Disponible: {producto.stock} | Solicitado: {cantidad}."
            )

        #Descontar stock y actualizar en la BD
        producto.stock -= cantidad
        self.dao.actualizar(producto)
        return producto
