import pytest

from exam import Inventario, Producto


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


def test_actualizar_producto_de_inventario():
    producto = Producto(1, 'Pantalones', 200.00, 50)
    inventario = Inventario()
    inventario.agregar_producto(producto)
    codigo = 1
    nuevo_precio = 500.00
    stock = 10
    inventario.actualizar_producto(codigo, nuevo_precio, stock)
    producto_actualizado = inventario.productos[1]
    assert producto_actualizado.codigo == codigo
    assert producto_actualizado.stock == stock
    assert producto_actualizado.precio == nuevo_precio
