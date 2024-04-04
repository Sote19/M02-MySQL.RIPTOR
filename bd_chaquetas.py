import random

# Lista de valores para generar datos aleatorios
talla_chaq = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
capucha_chaq = ["1", "0"]
corte_chaq = ["Entallado", "Regular", "Oversize", "Bomber", "Blazer", "Corte recto", "Corte ajustado", "Corte acolchado", "Corte cruzado", "Corte de motociclista"]

# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Generar el INSERT con los registros y el contador
insert = "INSERT INTO Chaquetas (id_producto, talla_chaq, capucha_chaq, corte_chaq) VALUES\n"
contador = 1276

for i in range(975):
    talla = valor_aleatorio(talla_chaq)
    capucha = valor_aleatorio(capucha_chaq)
    corte = valor_aleatorio(corte_chaq)    
    
    # Agregar los valores al INSERT
    insert += f"({contador}, '{talla}', '{capucha}', '{corte}'),\n"
    contador += 1

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)

