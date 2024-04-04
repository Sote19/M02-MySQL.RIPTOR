import random

# Lista de valores para generar datos aleatorios
talla_cami = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
corte_cami = ["Ajustado", "Regular", "Holgado", "Corte en V", "Cuello redondo", "Cuello en pico", "Sin mangas", "Manga corta", "Manga larga", "Manga raglán"]

# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Generar el INSERT con los 5000 registros
insert = "INSERT INTO Camisetas (id_producto, talla_cami, corte_cami) VALUES\n"
contador = 1

for i in range(1275):
    talla = valor_aleatorio(talla_cami)
    corte = valor_aleatorio(corte_cami)
    
    # Agregar los valores al INSERT
    insert += f"({contador}, '{talla}', '{corte}'),\n"
    contador += 1

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)
