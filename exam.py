class Producto:
    """
    Representa un producto individual con sus atributos.

    Args:
        codigo (int): Código único del producto.
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        stock (int): Cantidad en stock del producto.
    """

    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        """
        Devuelve string en representación del producto.
        """
        return f"{self.codigo} {self.nombre} {self.precio} {self.stock}"

class Inventario:
    """
    Representa un inventario de productos.

    Attributes:
        productos (dict): Diccionario que almacena los productos por su código.
    """

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario.

        Args:
        producto (Producto): Objeto de la clase Producto a agregar.
        """
        self.productos[producto.codigo] = producto

    def eliminar_producto(self, codigo):
        """
        Elimina un producto del inventario.

        Args:
        codigo (str): Código único del producto.
        """
        del self.productos[codigo]

    def actualizar_producto(self, codigo, nuevo_precio, stock):
        """
        Actualiza un producto del inventario.

        Args:
        codigo (int): Código único del producto.
        nuevo_precio (float): Nuevo precio del producto.
        stock (int): Cantidad en stock del producto.
        """
        self.productos[codigo].precio = nuevo_precio
        self.productos[codigo].stock = stock

    def mostrar_productos(self):
        print("========================================")
        print("Lista de Productos:")
        print("========================================")
        for producto in self.productos.values():
            print(producto)


# Crear instancia de la clase Inventario
inventario = Inventario()

# Agregar productos iniciales
inventario.agregar_producto(Producto(1, 'Pantalones', 200.00, 50))
inventario.agregar_producto(Producto(2, 'Camisas', 120.00, 45))
inventario.agregar_producto(Producto(3, 'Corbatas', 50.00, 30))
inventario.agregar_producto(Producto(4, 'Casacas', 350.00, 15))

# Bucle principal
while True:
    inventario.mostrar_productos()
    opcion = int(input("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir\nElija opción: "))
    if opcion == 1:
        codigo = int(input("Ingrese el código del nuevo producto: "))
        nombre = input("Ingrese el nombre del nuevo producto: ")
        precio = float(input("Ingrese el precio del nuevo producto: "))
        cantidad = int(input("Ingrese la cantidad en stock del nuevo producto: "))
        inventario.agregar_producto(Producto(codigo, nombre, precio, cantidad))
    elif opcion == 2:
        codigo = int(input("Ingrese el código del producto a eliminar: "))
        inventario.eliminar_producto(codigo)
    elif opcion == 3:
        codigo = int(input("Ingrese el código del producto a actualizar: "))
        nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
        nueva_cantidad = int(input("Ingrese la nueva cantidad en stock del producto: "))
        inventario.actualizar_producto(codigo, nuevo_precio, nueva_cantidad)
    elif opcion == 4:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
