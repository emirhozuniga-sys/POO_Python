class Producto: 
    def __init__(self, nombre: str, cantidad: int, precio: float):
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

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        if producto.nombre in self.productos:
            raise ValueError("El producto ya existe en el inventario.")
        else:
            self.productos[producto.nombre] = producto

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

def menu_principal():
    while True:
        print("1. Agregar producto ")
        print("2. Buscar producto ")
        print("3. Calcular valor total del inventario ")
        print("4. Listar todos los productos ")
        print("5. Salir ")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1": 
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                producto = Producto(nombre, cantidad, precio)
                inventario.agregar_producto(producto)
                print("Producto agregado exitosamente.")
            case "2":
                nombre = input("Ingrese el nombre del producto a buscar: ")
                producto = inventario.buscar_producto(nombre)
                if producto:
                    print(f"Producto encontrado: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
                else:
                    print("Producto no encontrado.")
            case "3":
                valor_total = inventario.calcular_valor_inventario()
                print(f"El valor total del inventario es: {valor_total}")
            case "4":
                productos = inventario.listar_productos()
                for producto in productos:
                    print(f"Producto: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
            case "5":
                print("Saliendo del programa.") 
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    inventario = Inventario()
    menu_principal()