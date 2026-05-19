# descuentos.py

def calcular_descuento(total_carrito: float, tipo_cliente: str) -> float:
    """
    Calcula el valor del descuento basado en el tipo de cliente y el monto total.
    
    Reglas iniciales de negocio (Fase Guiada):
    - Clientes 'VIP' obtienen 20% de descuento directo.
    - Clientes 'REGULAR' obtienen 5% si la compra supera los 100 dólares/unidades.
    - Valores negativos o menores a cero devuelven 0.0.
    """
    if total_carrito <= 0:
        return 0.0
        
    if tipo_cliente.upper() == "VIP":
        return total_carrito * 0.20
        
    elif tipo_cliente.upper() == "REGULAR" and total_carrito > 100:
        return total_carrito * 0.05
        
    return 0.0