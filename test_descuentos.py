# test_descuentos.py

import pytest
# Importamos la función que escribimos en el otro archivo
from descuentos import calcular_descuento

def test_descuento_vip():
    """Prueba que un cliente VIP reciba el 20% de descuento correctamente."""
    # Arrange (Preparar) & Act (Actuar)
    resultado = calcular_descuento(500.0, "VIP")
    # Assert (Afirmar/Validar): 20% de 200 es 40
    assert resultado == 40.0

def test_descuento_regular_mayor_a_cien():
    """Prueba que un cliente REGULAR con compra > 100 reciba el 5%."""
    resultado = calcular_descuento(200.0, "REGULAR")
    assert resultado == 10.0

def test_descuento_regular_menor_a_cien():
    """Prueba que un cliente REGULAR con compra <= 100 no reciba descuento."""
    resultado = calcular_descuento(50.0, "REGULAR")
    assert resultado == 0.0

def test_carrito_vacio_o_negativo():
    """Prueba el comportamiento con valores extremos o inválidos."""
    assert calcular_descuento(-50.0, "VIP") == 0.0
    assert calcular_descuento(0.0, "REGULAR") == 0.0