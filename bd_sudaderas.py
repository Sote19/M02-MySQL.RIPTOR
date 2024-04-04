import random

# Lista de valores para generar datos aleatorios
talla_suda = ["36", "38", "40", "42", "44", "46", "48", "50", "52", "54", "56", "XS", "S", "M", "L", "XL", "XXL", "XXXL"]
capucha_suda = ["1", "0"]
tipobolsillo_suda = ["Canguro", "Bolsillo tipo parche", "Bolsillo tipo ojal", "Bolsillo con cremallera", "Bolsillo tipo cierre magnético", "Bolsillo tipo fuelle", "Bolsillo tipo cierre de botón", "Bolsillo tipo escondido", "Bolsillo tipo divisor", "Bolsillo tipo bolsa interna"]
corte_suda = ["Clásico", "Entallado", "Oversize", "Crop top", "Corte asimétrico", "Corte holgado", "Corte ajustado", "Corte raglán", "Corte cropped", "Corte largo"]

# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Generar el INSERT con los registros y el contador
insert = "INSERT INTO Sudaderas (id_producto, talla_suda, capucha_suda, tipobolsillo_suda, corte_suda) VALUES\n"
foren_key = 3951

for i in range(525):
    talla = valor_aleatorio(talla_suda)
    capucha = valor_aleatorio(capucha_suda)
    tipobolsillo = valor_aleatorio(tipobolsillo_suda)
    corte = valor_aleatorio(corte_suda)
    
    # Agregar los valores al INSERT
    insert += f"({foren_key}, '{talla}', '{capucha}', '{tipobolsillo}', '{corte}'),\n"
    foren_key += 1

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)
