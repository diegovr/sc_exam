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
