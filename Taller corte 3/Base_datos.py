import sqlite3

class BaseDatos:
    # Nombre del archivo de la base de datos SQLite
    NOMBRE_DB = "inventario.db"

    @classmethod
    def conectar(cls):
        #Establecer y retornar la conexión usando la clase
        return sqlite3.connect(cls.NOMBRE_DB)

    @classmethod
    def crear_tabla(cls):
      
        conexion = cls.conectar()
        
        cursor = conexion.cursor()
        
        # Ejecutar la sentencia SQL para crear la tabla si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        """)
        
        
        conexion.commit()
        
        conexion.close()
