# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto de descuento aplicando un porcentaje al monto total.

    Parámetros:
        monto_total (float): valor total de la compra
        porcentaje_descuento (float): porcentaje de descuento a aplicar (por defecto 10)

    Retorna:
        float: monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
# 1ra llamada: solo monto total (usa el descuento por defecto del 10%)
monto1 = 130
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

# 2da llamada: monto total con porcentaje de descuento personalizado
monto2 = 210
descuento2 = calcular_descuento(monto2, 20)  # 15% de descuento
monto_final2 = monto2 - descuento2

# Mostrar resultados
print("Compra 1:")
print(f" Monto total: ${monto1}")
print(f" Descuento aplicado: ${descuento1}")
print(f" Monto final a pagar: ${monto_final1}")

print("\nCompra 2:")
print(f" Monto total: ${monto2}")
print(f" Descuento aplicado: ${descuento2}")
print(f" Monto final a pagar: ${monto_final2}")
