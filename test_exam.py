import pytest
from inventario import Inventario, Producto


def test_crear_producto():
    producto = Producto(1, 'Pantalones', 200.00, 50)
    assert producto.codigo == 1
    assert producto.nombre == 'Pantalones'
    assert producto.precio == 200.00
    assert producto.stock == 50

def test_agregar_producto_a_inventario():
    inventario = Inventario()
    producto = Producto(1, 'Pantalones', 200.00, 50)
    inventario.agregar_producto(producto)
    assert len(inventario.productos) == 1
    assert inventario.productos[1] == producto

def test_eliminar_producto_de_inventario():
    inventario = Inventario()
    producto = Producto(1, 'Pantalones', 200.00, 50)
    inventario.agregar_producto(producto)
    inventario.eliminar_producto(1)
    assert len(inventario.productos) == 0
