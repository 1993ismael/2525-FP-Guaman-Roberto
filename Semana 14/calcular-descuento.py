def calcular_descuento(monto_compra, porcentaje_descuento=10):
    monto_descuento = monto_compra * (porcentaje_descuento / 100)
    total_pagar = monto_compra - monto_descuento
    return monto_descuento, total_pagar

# Datos de ejemplo
monto = 200
descuento = 12

monto_desc, total = calcular_descuento(monto, descuento)

print(f"Monto de la compra: ${monto:.2f}")
print(f"Descuento aplicado ({descuento}%): ${monto_desc:.2f}")
print(f"Total a pagar: ${total:.2f}")