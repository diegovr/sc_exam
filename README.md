# sc_exam
Soy Calidad exam

Este ejercicio esta desarrollado en [![python](https://img.shields.io/badge/Python-3.11.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

# Ejercicio #1
```plaintext
Elaborar un programa que muestre los diccionarios, y programar las
siguientes acciones:
# [1] Agregar
# [2] Eliminar
# [3] Actualizar
# [4] Salir
========================================
Lista de Productos:
========================================
1 Pantalones 200.0 50
2 Camisas 120.0 45
3 Corbatas 50.0 30
4 Casacas 350.0 15
========================================
[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir
Elija opción:
```

## Requerimientos
Antes de ejecutar o probar este ejercicio es necesario instalar algunos paquetes, para si utiliza un terminal o consola, deberá posicionarse en el directorio donde clonó este repositorio:

{% filename %}command-line{% endfilename %}

    $ cd path/del/proyecto/
    $ git clone git@git...
    $ cd sc_exam/
    
Luego instalar las dependencias, para eso ejecute:

    $ pip install -r requirements.txt

Y finalmente para correr el ejercicio, ejecute la siguiente linea de comando:

    $ python sc_exam.py

Y siga las instrucciones.

## Pruebas

Para ejecutar las pruebas de unidad, ejecute la siguiente linea de comando:

    $ pytest test_exam.py

Para comprobar que todas las pruebas se realizaron con éxito le retornará un mensaje como el siguiente:
```
========================================== test session starts ======================================
platform darwin -- Python 3.11.9, pytest-8.3.2, pluggy-1.5.0
rootdir: /path/del/proyecto/sc_exam
collected 4 items

test_exam.py ....                                                                              [100%]

============================================ 4 passed in 0.02s ======================================
```
