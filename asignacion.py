import math  # Usamos π

# Valor real
real = math.pi  

# Pedimos cuántos decimales usar
decimales = int(input("Ingrese cantidad de decimales: "))

# Factor para mover el decimal
factor = 10 ** decimales

# Redondeo (al número más cercano)
redondeado = round(real, decimales)

# Truncamiento (corta decimales)
truncado = int(real * factor) / factor

# Calculamos errores
error_redondeo = abs(real - redondeado)
error_trunc = abs(real - truncado)

# Mostramos resultados
print("\nValor real:", real)

print("\nRedondeado:", redondeado)
print("Error redondeo:", error_redondeo)

print("\nTruncado:", truncado)
print("Error truncamiento:", error_trunc)

# Comparamos errores
if error_trunc > error_redondeo:
    print("\nTruncamiento tiene más error")
else:
    print("\nRedondeo tiene más error")