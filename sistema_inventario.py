class Producto: 
    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not nombre:
            raise ValueError("El nombre del producto no puede estar vacío.")
        else:
            self.nombre = nombre
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        else:
            self.cantidad = cantidad
        
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        else:   
            self.precio = precio
    
    def actualizar_precio(self,nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        else:
            self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad: int):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        else:
            self.cantidad = nueva_cantidad

    def calcular_valor_total(self) -> float:
        return self.cantidad * self.precio

    def __str__(self):
        return f"Producto(Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio})"

class Inventario:
    def __init__(self):
        self.productos: dict[str, Producto] = {}

    def agregar_producto(self, producto: Producto):
        nombre_clave = producto.nombre.lower()
        if nombre_clave in self.productos:
            # Actualizar cantidad si el producto ya existe
            self.productos[nombre_clave].actualizar_cantidad(
                self.productos[nombre_clave].cantidad + producto.cantidad
            )
        else:
            self.productos[nombre_clave] = producto

    def buscar_producto(self, nombresf: str) -> Producto:
        nombre = nombresf.lower()
        if nombre in self.productos:
            return self.productos[nombre]
        else:
            return None
    
    def calcular_valor_inventario(self) -> float:
        valor_total = 0.0
        for producto in self.productos.values():
            valor_total += producto.cantidad * producto.precio
        return valor_total
    
    def listar_productos(self) -> list:
        return list(self.productos.values())
    

    ### Main program ####

def leer_entero(mensaje: str) -> int:
    """Lee un entero del usuario con reintentos hasta obtener un valor válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def leer_flotante(mensaje: str) -> float:
    """Lee un número flotante del usuario con reintentos hasta obtener un valor válido."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Ingrese un número decimal válido.")

def leer_nombre(mensaje: str) -> str:
    """Lee un nombre del usuario con reintentos hasta obtener un valor no vacío."""
    while True:
        nombre = input(mensaje).strip()
        if nombre:
            return nombre
        else:
            print("Error: El nombre no puede estar vacío.")

def manejar_agregar_producto():
    """Maneja la opción de agregar un nuevo producto."""
    try:
        nombre = leer_nombre("Ingrese el nombre del producto: ")
        cantidad = leer_entero("Ingrese la cantidad del producto: ")
        precio = leer_flotante("Ingrese el precio del producto: ")
        producto = Producto(nombre, cantidad, precio)
        inventario.agregar_producto(producto)
        print("✓ Producto agregado exitosamente.")
    except ValueError as e:
        print(f"✗ Error al agregar producto: {e}")
    except Exception as e:
        print(f"✗ Error inesperado: {e}")

def manejar_buscar_producto():
    """Maneja la opción de buscar un producto."""
    try:
        nombre = leer_nombre("Ingrese el nombre del producto a buscar: ")
        producto = inventario.buscar_producto(nombre)
        if producto:
            print(f"✓ Producto encontrado: {producto}")
        else:
            print("✗ Producto no encontrado.")
    except Exception as e:
        print(f"✗ Error al buscar producto: {e}")

def manejar_calcular_valor():
    """Maneja la opción de calcular el valor total del inventario."""
    try:
        valor_total = inventario.calcular_valor_inventario()
        print(f"✓ El valor total del inventario es: ${valor_total:.2f}")
    except Exception as e:
        print(f"✗ Error al calcular valor: {e}")

def manejar_listar_productos():
    """Maneja la opción de listar todos los productos."""
    try:
        productos = inventario.listar_productos()
        if productos:
            print("\n--- PRODUCTOS EN INVENTARIO ---")
            for producto in productos:
                print(f"  • {producto}")
            print()
        else:
            print("✗ El inventario está vacío.")
    except Exception as e:
        print(f"✗ Error al listar productos: {e}")

def menu_principal():
    """Menú principal interactivo del sistema de inventario."""
    while True:
        try:
            print("\n" + "="*40)
            print("    SISTEMA DE INVENTARIO")
            print("="*40)
            print("1. Agregar producto")
            print("2. Buscar producto")
            print("3. Calcular valor total del inventario")
            print("4. Listar todos los productos")
            print("5. Salir")
            print("="*40)
            opcion = input("Seleccione una opción: ").strip()

            match opcion:
                case "1": 
                    manejar_agregar_producto()
                case "2":
                    manejar_buscar_producto()
                case "3":
                    manejar_calcular_valor()
                case "4":
                    manejar_listar_productos()
                case "5":
                    print("Saliendo del programa...") 
                    break
                case _:
                    print("✗ Opción no válida. Intente de nuevo.")
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado en el menú: {e}")
if __name__ == "__main__":
    inventario = Inventario()
    menu_principal()