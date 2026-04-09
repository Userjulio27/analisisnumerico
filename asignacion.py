# Programa de error de redondeo

# Pedir datos al usuario
valor_real = float(input("Ingrese el valor real: "))
valor_aproximado = float(input("Ingrese el valor aproximado: "))

# Calcular errores
error_absoluto = abs(valor_real - valor_aproximado)

if valor_real != 0:
    error_relativo = error_absoluto / abs(valor_real)
    error_porcentual = error_relativo * 100
else:
    error_relativo = 0
    error_porcentual = 0

# Mostrar resultados
print("\n--- RESULTADOS ---")
print("Error absoluto:", error_absoluto)
print("Error relativo:", error_relativo)
print("Error porcentual:", error_porcentual, "%")