import random

# Lista de valores para generar datos aleatorios
talla_lenceria_inter = ["XS", "S", "M", "L", "XL", "XXL", "XXXL", "34", "36", "38", "40", "42", "44", "46", "48", "50", "52", "54", "56"]
conjunto_inter = ["1", "0"]

# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Generar el INSERT con los registros y el contador
insert = "INSERT INTO Ropa_interior (id_producto, talla_lenceria_inter, conjunto_inter) VALUES\n"
contador = 2526

for i in range(275):
    talla = valor_aleatorio(talla_lenceria_inter)
    conjunto = valor_aleatorio(conjunto_inter)
    
    # Agregar los valores al INSERT
    insert += f"({contador}, '{talla}', '{conjunto}'),\n"
    contador += 1

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)
