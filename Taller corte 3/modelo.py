class Producto:
    """Representa la entidad Producto (videojuego) en el sistema."""

    def __init__(self, nombre: str, precio: float, stock: int, id: int = None):
        # Paso 1: Asignar ID (None si es nuevo, o número si viene de la BD)
        self.id = id
       
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def __str__(self) -> str:
        # Formato de texto para mostrar el producto en consola
        return f"ID: {self.id} | Videojuego: {self.nombre} | Precio: ${self.precio:,.2f} | Stock: {self.stock} unidades"
